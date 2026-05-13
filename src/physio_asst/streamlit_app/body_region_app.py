# src/physio_asst/streamlit_app/body_region_app.py

import streamlit as st
from openai import OpenAI
import google.generativeai as genai
import os
import re

ENV_KEY_NAMES = {
    "google_genai": "GOOGLE_GENAI_API_KEY",
    "deepseek": "DEEPSEEK_API_KEY",
}

def get_api_key(secret_key: str, session_key: str):
    """
    Fetch an API key without hardcoding credentials.

    Priority:
      1. User-supplied (from app.py sidebar -> st.session_state)
      2. Streamlit secrets.toml / Streamlit Cloud Secrets
      3. Environment variables
    """
    session_value = st.session_state.get(session_key)
    if isinstance(session_value, str):
        session_value = session_value.strip()
    if session_value:
        st.info(f"Using user-supplied {secret_key} API key.")
        return session_value

    try:
        secret_value = st.secrets["api_keys"][secret_key]
        if secret_value:
            st.info(f"Loaded {secret_key} API key from Streamlit secrets.")
            return secret_value.strip()
    except (KeyError, AttributeError):
        pass

    env_name = ENV_KEY_NAMES.get(secret_key)
    if env_name:
        env_value = os.environ.get(env_name, "").strip()
        if env_value:
            st.info(f"Loaded {secret_key} API key from {env_name}.")
            return env_value

    return None


def require_api_key(secret_key: str, session_key: str, provider_label: str):
    api_key = get_api_key(secret_key, session_key)
    if not api_key:
        st.warning(
            f"Missing {provider_label} API key. Provide it in the sidebar, "
            f"Streamlit secrets under [api_keys].{secret_key}, or {ENV_KEY_NAMES.get(secret_key, 'an environment variable')}."
        )
    return api_key


def rerun_app():
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()

# -------------------------------
# HELPER FUNCTION – Formatting AI output
# -------------------------------
def format_diagnosis_output(raw_text, color):
    """Format AI diagnosis so only the diagnosis lines (1., 2., 3.) are bold and colored, not the reasoning."""
    # only the first numbered line onward
    cleaned = re.sub(r"(?is)^.*?(?=\n?1\.)", "", raw_text).strip()
    # Split into numbered sections (1., 2., 3., ...)
    parts = re.split(r"(?=\n?\d+\.)", cleaned)
    formatted_parts = []
    for part in parts:
        if not part.strip():
            continue
        # First line = diagnosis header
        lines = part.strip().split("\n", 1)
        header = lines[0].strip()
        reasoning = lines[1].strip() if len(lines) > 1 else ""

        # Apply color/bold only to the header (diagnosis line)
        header_html = f"<b><span style='color:{color};'>{header}</span></b>"
        if reasoning:
            formatted_parts.append(f"{header_html}<br>{reasoning}")
        else:
            formatted_parts.append(header_html)

    return "<br><br>".join(formatted_parts)
    
# -------------------------------
# MAIN FUNCTION – Runs the 4-step workflow
# -------------------------------
def run_body_region_app(
    region_name,
    system_prompt,
    compare_prompt,
    qa_prompt,
    rehab_links,
    prefilled_example=None,
):
    st.header(f"🩺  {region_name} Diagnosis Assistant")
    # -------------------------------
    # MODEL SELECTION
    # -------------------------------
    MODEL_PROVIDER = st.radio("Select LLM Model:", ["Gemini", "DeepSeek"])
    TEMPERATURE, TOP_P = 0.7, 0.95
    #st.markdown(
    #    "<p style='color:red; font-weight:bold;'>⚠️ 🇨🇳大陆用户 DeepSeek.</p>",
    #    unsafe_allow_html=True,
    #)

    # -------------------------------
    # STEP 1 – radiology analysis 
    # -------------------------------    
    st.text(f"Enter your radiology exam (e.g., MRI, ultrasound, x-ray) description and get LLM-predicted top 3 {region_name.lower()} conditions.")
    #st.text(f"An example for my poor shoulder: pages/examples.txt  ")
    description_label = "description here"
    if prefilled_example:
        description_label += " (a prefilled example attached in the box)"
    mri_text = st.text_area(
        description_label,
        value=prefilled_example or "",
        placeholder=f"Paste description ONLY for {region_name}",
        height=280 if prefilled_example else 150,
    )
    
    full_response_text = ""

    if st.button("🔍 Run Diagnosis"):
        if not mri_text.strip():
            st.warning("Please enter exam description first.")
        else:
            success = False

            try:
                if MODEL_PROVIDER == "Gemini":
                    google_key = require_api_key("google_genai", "google_api_key", "Google Gemini")
                    if google_key:
                        genai.configure(api_key=google_key)
                        model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=system_prompt)
                        st.markdown("##### 🔴 Google Gemini thinks:")
                        with st.spinner("Gemini is analyzing..."):
                            response = model.generate_content(mri_text, stream=False)
                            full_response_text = response.text
                            formatted = format_diagnosis_output(full_response_text, "red")
                            st.markdown(formatted, unsafe_allow_html=True)
                            success = True

                elif MODEL_PROVIDER == "DeepSeek":
                    deepseek_key = require_api_key("deepseek", "deepseek_api_key", "DeepSeek")
                    if deepseek_key:
                        client = OpenAI(
                            api_key=deepseek_key,
                            base_url="https://api.deepseek.com",
                        )
                        st.markdown("##### 🟢 DeepSeek thinks:")
                        with st.spinner("DeepSeek is analyzing..."):
                            response = client.chat.completions.create(
                                model="deepseek-chat",
                                messages=[
                                    {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": mri_text},
                                ],
                                temperature=TEMPERATURE,
                                stream=False,
                            )
                            full_response_text = response.choices[0].message.content
                            formatted = format_diagnosis_output(full_response_text, "green")
                            st.markdown(formatted, unsafe_allow_html=True)
                            success = True
            except Exception as exc:
                st.error(f"{MODEL_PROVIDER} request failed: {exc}")

            if success:
                st.session_state["mri_text"] = mri_text
                st.session_state["diagnosis_result"] = full_response_text
                st.session_state["model_provider"] = MODEL_PROVIDER

    # -------------------------------
    # STEP 2 – EXERCISE PLAN LINKS (INTERACTIVE)
    # -------------------------------
    if "diagnosis_result" in st.session_state and st.session_state["diagnosis_result"]:
        st.markdown("---")
        st.subheader(f"🏋️‍♀️ At-home exercise plans for {region_name.capitalize()}")
        st.text("reference: https://purephysiotherapy.co.uk/")
    
        # Extract top 3 diagnosed conditions from model output
        diag_text = st.session_state["diagnosis_result"]
    
        # Find matching conditions safely
        diagnosed_conditions = [
            cond for cond in rehab_links.keys()
            if isinstance(cond, str) and cond.lower() in diag_text.lower()
        ][:3]
    
        if diagnosed_conditions:
            selected = st.multiselect(
                "Select one or more diagnosed conditions to view their rehab plan:",
                diagnosed_conditions,
                default=diagnosed_conditions[:1],
            )
    
            for cond in selected:
                url = rehab_links.get(cond, None)
                if url:
                    st.markdown(f"- [{cond} – view least painful programme →]({url})")
                else:
                    st.write(f"- Plans for {region_name} are coming soon...")
        else:
            st.info("No matching conditions found in the diagnosis output yet.")
    else:
        st.warning("⚠️ At-home rehab plans will be provided for you after LLM-predicted diagnosis on your report.")



    


    # -------------------------------
    # STEP 3 – DOCTOR COMPARISON
    # -------------------------------
    if "diagnosis_result" in st.session_state:
        st.markdown("---")
        st.subheader("🧠 Compare two OPPOSITE doctors opinions")
        
        doc1, doc2 = st.columns(2, gap="medium")
        with doc1:
            opinion1 = st.text_area("Doctor 1’s Opinion 医生1意见", placeholder=f"only for {region_name} related questions for this page.", height=100)
        with doc2:
            opinion2 = st.text_area("Doctor 2’s Opinion 医生2意见", placeholder=f"only for {region_name} related questions for this page.", height=100)


        if st.button("⚖️ Compare opinions"):
            mri = st.session_state.get("mri_text", "")
            diagnosis = st.session_state.get("diagnosis_result", "")
            history = st.session_state.get("comparison_result", "")
            
            compare_prompt_filled = compare_prompt.format(
                mri=mri,
                diagnosis=diagnosis,
                history=history
            )

            if not opinion1 or not opinion2:
                st.warning("Please fill in both opinions.")
            else:
                user_input = f"Doctor 1: {opinion1}\n\nDoctor 2: {opinion2}"
                provider = st.session_state.get("model_provider", MODEL_PROVIDER)
                
                try:
                    if provider == "Gemini":
                        google_key = require_api_key("google_genai", "google_api_key", "Google Gemini")
                        if not google_key:
                            return
                        genai.configure(api_key=google_key)
                        model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=compare_prompt_filled)
                        with st.spinner("Gemini is comparing..."):
                            response = model.generate_content(user_input, stream=False)
                            result_text = response.text
                    else:
                        deepseek_key = require_api_key("deepseek", "deepseek_api_key", "DeepSeek")
                        if not deepseek_key:
                            return
                        client = OpenAI(
                            api_key=deepseek_key,
                            base_url="https://api.deepseek.com",
                        )
                        with st.spinner("DeepSeek is comparing..."):
                            response = client.chat.completions.create(
                                model="deepseek-chat",
                                messages=[
                                    {"role": "system", "content": compare_prompt_filled},
                                    {"role": "user", "content": user_input},
                                ],
                                temperature=TEMPERATURE,
                                stream=False,
                            )
                            result_text = response.choices[0].message.content
                except Exception as exc:
                    st.error(f"{provider} comparison request failed: {exc}")
                    return

                st.markdown("### 💬 AI’s Comparative Evaluation")
                st.info(result_text)
                st.session_state["comparison_result"] = result_text



    
    # -------------------------------
    # STEP 4 – Q-A (INTERACTIVE)
    # -------------------------------
    def _extract_followups(block_text: str):
        """Extract follow-ups robustly even if Gemini adds spaces or invisible chars."""
        out = []
        for line in block_text.splitlines():
            # Normalize invisible spaces and colons
            s = line.replace("\uFEFF", "").replace("\u202F", "").strip("  ").strip()
            if s.lstrip("•*-—–> ").startswith("❓"):
                out.append(s.lstrip("•*-—–> ❓").strip())
            elif "❓" in s and len(s) < 200:
                # backup: any short line containing ❓ looks like a follow-up
                out.append(s[s.index("❓") + 1 :].strip())
        return out
    
    def _model_reply(provider, prompt_with_context, user_message):
        """Unified model call for Gemini / DeepSeek."""
        if provider == "Gemini":
            google_key = require_api_key("google_genai", "google_api_key", "Google Gemini")
            if not google_key:
                return None
            genai.configure(api_key=google_key)
            qa_model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=prompt_with_context)
            with st.spinner("Gemini is responding..."):
                resp = qa_model.generate_content(user_message, stream=False)
            return resp.text
    
        elif provider == "DeepSeek":
            deepseek_key = require_api_key("deepseek", "deepseek_api_key", "DeepSeek")
            if not deepseek_key:
                return None
            client = OpenAI(
                api_key=deepseek_key,
                base_url="https://api.deepseek.com",
            )
            with st.spinner("DeepSeek is responding..."):
                resp = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": prompt_with_context},
                        {"role": "user", "content": user_message},
                    ],
                    temperature=TEMPERATURE,
                    stream=False,
                )
            return resp.choices[0].message.content
    
        else:
            st.error("Invalid provider.")
            return None
    
    # -------------------------------------------
    # MAIN Q&A INTERFACE
    # -------------------------------------------
    st.markdown("---")
    st.subheader("💬 Interactive Q&A – ask any other questions")
    
    st.markdown(
        "<p>You can ask about pain, exercises, or rehab advice. "
        "The AI will first answer all your questions briefly, "
        "then ask follow-up questions to personalize its advice.</p>",
        unsafe_allow_html=True,
    )
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    if "qa_threads" not in st.session_state:
        st.session_state.qa_threads = []
    
    # -----------------------
    # Collect user questions
    # -----------------------
    user_questions_block = st.text_area(
        "Enter all your questions here (one per line or numbered):",
        placeholder="1. 如果运动的话，需要带护具还是运动绑带更好？\n2. 我现在吃celecoxib，可以喝酒吗？",
        height=150,
        key="step3_user_questions",
    )
    
    if st.button("🔍 Analyze list"):
        if not user_questions_block.strip():
            st.warning("Please enter at least one question.")
        else:
            # Split into numbered list
            qs = re.split(r"\n?\d+\.\s*|\n+", user_questions_block.strip())
            qs = [q.strip() for q in qs if q.strip()]
            st.session_state.qa_threads = [
                {"q": q, "history": [], "pending": [], "done": False} for q in qs
            ]
    
            provider = st.session_state.get("model_provider", MODEL_PROVIDER)
            qa_prompt_text = qa_prompt.format(
                mri=st.session_state.get("mri_text", ""),
                diagnosis=st.session_state.get("diagnosis_result", ""),
                history=""
            )
    
            # --- Strong output contract for consistent answers ---
            user_msg = f"""
    You will receive {len(qs)} user questions about one body region.
    
    REQUIRED OUTPUT FORMAT:
    For each question i (i = 1..N), produce exactly:
    i. <Short answer to question i (2–4 sentences)>
       (optional) ❓<ONE clarifying follow-up for that same question>
    
    Rules:
    - Include every i from 1..N — no omissions.
    - Each answer must start with "i." on its own line (e.g., "1.", "2.", "3.").
    - If clarification is needed, add ONE follow-up on the next line starting with "❓".
    - Keep each item independent; do NOT mix follow-ups between items.
    
    User questions:
    {chr(10).join([f"{i+1}. {q}" for i, q in enumerate(qs)])}
    """
    
            try:
                ai_text = _model_reply(provider, qa_prompt_text, user_msg)
            except Exception as exc:
                st.error(f"{provider} Q&A request failed: {exc}")
                ai_text = None
            if not ai_text:
                return
    
            # --- Parse the model output into per-question blocks ---
            blocks = re.split(r"(?m)^(?=\d+\.\s)", ai_text.strip())
            blocks = [b.strip() for b in blocks if b.strip()]
    
            for j, q in enumerate(qs):
                ans = blocks[j] if j < len(blocks) else "No answer produced for this item."
                st.session_state.qa_threads[j]["history"].append((q, ans))
                st.session_state.qa_threads[j]["pending"] = _extract_followups(ans)
    
            rerun_app()
 
    # -----------------------
    # DISPLAY SECTION
    # -----------------------
    if st.session_state.qa_threads:
        threads = st.session_state.qa_threads
        st.markdown(f"### Working on all {len(threads)} questions")
    
        for i, th in enumerate(threads):
            # --- Grey-out style for completed questions ---
            if th.get("done"):
                with st.expander(f"✅ Q{i+1}: {th['q']}", expanded=False):
                    st.markdown(
                        f"""
                        <div style='background-color:#f2f2f2; color:#666; padding:10px; border-radius:8px;'>
                            <b>💬 Assistant’s final reply:</b><br>
                            {th['history'][-1][1] if th['history'] else '(no reply recorded)'}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                continue
    
            # --- Normal active question display ---
            st.markdown(f"**🗣 Question {i+1}:** {th['q']}")
            if th["history"]:
                _, last_a = th["history"][-1]
                st.markdown("**💬 Assistant’s reply:**")
                st.info(last_a)
    
            # --- Handle per-item follow-up interaction ---
            if th["pending"]:
                fu = th["pending"][0]
                with st.form(key=f"fu_form_{i}", clear_on_submit=True):
                    st.markdown(
                        f"<span style='color:orange; font-weight:600;'>❓ Follow-up for Q{i+1}:</span> {fu}",
                        unsafe_allow_html=True,
                    )
                    fu_answer = st.text_input("Your answer:")
                    cols = st.columns([3, 1])
                    with cols[0]:
                        send_fu = st.form_submit_button("Send follow-up")
                    with cols[1]:
                        mark_done_here = st.form_submit_button(f"✅ Mark Q{i+1} done")
    
                if send_fu and fu_answer.strip():
                    hist_txt = "\n".join([f"User: {u}\nAI: {a}" for (u, a) in th["history"]])
                    sys_prompt = qa_prompt.format(
                        mri=st.session_state.get("mri_text", ""),
                        diagnosis=st.session_state.get("diagnosis_result", ""),
                        history=hist_txt,
                    )
                    user_follow = (
                        f"Follow-up answer to: {fu}\n"
                        f"User reply: {fu_answer}\n\n"
                        "Refine ONLY the advice for this question. "
                        "If another clarification is needed for THIS item, add ONE new ❓ line."
                    )
                    try:
                        with st.spinner(f"Refining Q{i+1}..."):
                            refined = _model_reply(st.session_state.get("model_provider", MODEL_PROVIDER), sys_prompt, user_follow)
                    except Exception as exc:
                        st.error(f"Follow-up request failed: {exc}")
                        refined = None
                    if not refined:
                        return
    
                    th["history"].append((f"(Follow-up) {fu}: {fu_answer}", refined))
                    th["pending"] = _extract_followups(refined)
                    rerun_app()
    
                elif mark_done_here:
                    th["done"] = True
                    th["pending"] = []
                    rerun_app()
    
            else:
                # No pending follow-ups
                if not th["done"]:
                    if st.button(f"✅ Mark Q{i+1} done", key=f"mark_done_btn_{i}"):
                        th["done"] = True
                        rerun_app()
