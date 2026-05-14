# 🩺 Physio Assistant App

### 🔗 **App URL:**   [Physio Assistant App](https://your-streamlit-app-url.streamlit.app/)

## Overview
**Physio Assistant** is an AI-powered interactive web app built with **Streamlit**, designed to help users understand their radiology findings and explore tailored at-home rehabilitation guidance.  

The app interprets radiology summaries using LLM, generates human-readable explanations, compares medical opinions, and offers follow-up interactive Q&A feedback — helping users bridge the gap between medical diagnostics and practical rehabilitation knowledge.  

It is an **educational and physiotherapy support tool**, not a substitute for professional diagnosis or clinical advice.

---

## 🚀 Key Features
- **AI radiology interpreter:** Translates MRI/x-ray/ ultrasound findings and suggest most likely conditions.  
- **Rehabilitation plan:** Suggests safe, evidence-based at-home rehab movements for your  conditions.  
- **Doctor comparison mode:** Displays and contrasts two different medical opinions, helping users visualize diagnostic discrepancies and treatment focus areas.  
- **Interactive Q&A assistant:** Users can ask any clarifying or follow-up questions — the AI responds contextually, providing ongoing educational feedback.  
- **Model comparison:** Allows switching between **Gemini** and **DeepSeek** engines for explanation quality benchmarking.  

---

## 🧠 Tech Stack
| Layer | Technology |
|-------|-------------|
| Front-end | [Streamlit](https://streamlit.io/) |
| LLM Modes | Google Gemini 2.5 Flash, DeepSeek API |

---

## 🧠 Local Setup

If Python is not installed yet, install it from the official site:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

On Windows, select **Add Python to PATH** during installation.

If Git is not installed yet, install it from:  
👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)

On Windows, you can run the commands below in **Git Bash**, PowerShell, or Command Prompt.

---

### 🪜 Run Steps (1 → 5) on MacOS

```bash
# 1. Clone the repository
git clone https://github.com/susierwu/physio.git
cd physio

# 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
python3 -m pip install -r requirements.txt

# 4. Create local Streamlit secrets file
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Then edit .streamlit/secrets.toml
# and paste your own API keys 

# 5. Start the app
streamlit run src/physio_asst/streamlit_app/app.py

```
