# src/physio_asst/streamlit_app/body_region_app.py

import streamlit as st
from openai import OpenAI
import google.generativeai as genai
import re

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
def run_body_region_app(region_name, system_prompt, compare_prompt, qa_prompt, rehab_links):
    st.header(f"🩺  {region_name} Diagnosis Assistant")
    # -------------------------------
    # MODEL SELECTION
    # -------------------------------
    MODEL_PROVIDER = st.radio("Select LLM Model:", ["Gemini", "DeepSeek"])
    TEMPERATURE, TOP_P = 0.7, 0.95
    st.markdown(
        "<p style='color:red; font-weight:bold;'>⚠️ 🇨🇳大陆用户 DeepSeek.</p>",
        unsafe_allow_html=True,
    )

    # -------------------------------
    # STEP 1 – radiology analysis 
    # -------------------------------    
    st.text(f"Enter your radiology exam (e.g., MRI, ultrasound, x-ray) description and get LLM-predicted top 3 {region_name.lower()} conditions.")
    #st.text(f"An example for my poor shoulder: pages/examples.txt  ")
    mri_text = st.text_area(f"description here", placeholder=f"Paste description ONLY for {region_name}", height=150)
    
    full_response_text = ""

    if st.button("🔍 Run Diagnosis"):
        if not mri_text.strip():
            st.warning("Please enter exam description first.")
        else:
            if MODEL_PROVIDER == "Gemini":
                genai.configure(api_key=st.secrets["api_keys"]["google_genai"])
                model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=system_prompt)
                st.markdown("##### 🔴 Google Gemini thinks:")
                with st.spinner("Gemini is analyzing..."):
                    response = model.generate_content(mri_text, stream=False)
                    formatted = format_diagnosis_output(response.text, "red")
                    st.markdown(formatted, unsafe_allow_html=True)
                    full_response_text = response.text

            elif MODEL_PROVIDER == "DeepSeek":
                client = OpenAI(
                    api_key=st.secrets["api_keys"]["deepseek"],
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
                    formatted = format_diagnosis_output(response.choices[0].message.content, "green")
                    st.markdown(formatted, unsafe_allow_html=True)
                    full_response_text = response.choices[0].message.content

            st.session_state["mri_text"] = mri_text
            st.session_state["diagnosis_result"] = full_response_text
            st.session_state["model_provider"] = MODEL_PROVIDER


    
    # -------------------------------
    # STEP 2 – DOCTOR COMPARISON
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
                provider = st.session_state["model_provider"]
                
                if provider == "Gemini":
                    genai.configure(api_key=st.secrets["api_keys"]["google_genai"])
                    model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=compare_prompt_filled)
                    with st.spinner("Gemini is comparing..."):
                        response = model.generate_content(user_input, stream=False)
                        result_text = response.text
                else:
                    client = OpenAI(
                        api_key=st.secrets["api_keys"]["deepseek"],
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

                st.markdown("### 💬 AI’s Comparative Evaluation")
                st.info(result_text)
                st.session_state["comparison_result"] = result_text



                
    # -------------------------------
    # STEP 3 – INTERACTIVE Q&A
    # -------------------------------
    if "diagnosis_result" in st.session_state:
        st.markdown("---")
        st.subheader("💬 Ask any other questions")

        st.markdown(
            "<p>You can ask about pain, exercises, or rehab advice. The AI will first answer briefly, "
            "then ask follow-up questions to personalize its advice.</p>",
            unsafe_allow_html=True,
        )

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_question = st.text_area(
            "Enter your question or reply:",
            placeholder="e.g., What exercises can I do safely now?",
            key="step4_user_input",
        )

        if st.button("🧩 Analyze your questions"):
            if not user_question.strip():
                st.warning("Please type a question first.")
            else:
                provider = st.session_state["model_provider"]
                mri_context = st.session_state.get("mri_text", "")
                diagnosis_context = st.session_state.get("diagnosis_result", "")

                conversation_context = "\n".join(
                    [f"User: {q}\nAI: {a}" for q, a in st.session_state.chat_history]
                )

                prompt_with_context = qa_prompt.format(
                    mri=st.session_state.get("mri_text", ""),
                    diagnosis=st.session_state.get("diagnosis_result", ""),
                    history="\n".join([f"User: {q}\nAI: {a}" for q, a in st.session_state.chat_history])
                )
                                
                full_context = f"User: {user_question}"

                if provider == "Gemini":
                    genai.configure(api_key=st.secrets["api_keys"]["google_genai"])
                    qa_model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=prompt_with_context)
                    with st.spinner("Gemini is responding..."):
                        resp = qa_model.generate_content(full_context, stream=False)
                        ai_reply = resp.text
                else:
                    client = OpenAI(
                        api_key=st.secrets["api_keys"]["deepseek"],
                        base_url="https://api.deepseek.com",
                    )
                    with st.spinner("DeepSeek is responding..."):
                        resp = client.chat.completions.create(
                            model="deepseek-chat",
                            messages=[
                                {"role": "system", "content": prompt_with_context},
                                {"role": "user", "content": full_context},
                            ],
                            temperature=TEMPERATURE,
                            stream=False,
                        )
                        ai_reply = resp.choices[0].message.content

                st.session_state.chat_history.append((user_question, ai_reply))

        if st.session_state.chat_history:
            last_q, last_a = st.session_state.chat_history[-1]
            st.markdown("### 🤖 Assistant's reply:")
            st.markdown(f"**🗣 Your question:** {last_q}")
            st.markdown(f"**💬 Assistant's response:**")
            st.info(last_a)  #same as ai_reply


        
    # -------------------------------
    # STEP 4 – EXERCISE PLAN LINKS (INTERACTIVE)
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
        st.warning("⚠️ At-home rehab plans will be provided for you after LLM-predicted diagnosis on your MRI.")


