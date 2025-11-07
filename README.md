# 🩺 Physio Assistant App

## Overview  
**Physio Assistant** is an AI-powered interactive web app built with **Streamlit**, designed to help users understand their radiology findings and explore tailored at-home rehabilitation guidance.  

The app interprets radiology summaries using LLM, generates human-readable explanations, compares medical opinions, and offers follow-up interactive Q&A feedback — helping users bridge the gap between medical diagnostics and practical rehabilitation knowledge.  

It is an **educational and physiotherapy support tool**, not a substitute for professional diagnosis or clinical advice.

---

## 🚀 Key Features
- **AI Radiology Interpreter:** Translates MRI/x-ray/ ultrasound findings and suggest most likely conditions.  
- **Rehabilitation Plan:** Suggests safe, evidence-based at-home rehab movements for your  conditions.  
- **Doctor Comparison Mode:** Displays and contrasts two different medical opinions, helping users visualize diagnostic discrepancies and treatment focus areas.  
- **Interactive Q&A Assistant:** Users can ask any clarifying or follow-up questions — the AI responds contextually, providing ongoing educational feedback.  
- **Model Comparison:** Allows switching between **Gemini** and **DeepSeek** engines for explanation quality benchmarking.  

---

## 🧠 Tech Stack
| Layer | Technology |
|-------|-------------|
| Front-end | [Streamlit](https://streamlit.io/) |
| LLM Modes | Google Gemini 2.0 Flash, DeepSeek API |

---

## 🧠 本地运行（macOS / Windows）

> 若尚未安装 Python，请先从官方页面安装最新版本：  
> 👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)  
> **务必在安装时勾选 “Add Python to PATH” 选项。**

---

### 🪜 运行步骤（1️⃣ → 5️⃣）

```bash
# 1️⃣ 克隆项目
git clone git@github.com:susierwu/physio.git
cd physio

# 2️⃣ 若提示 pip 不存在，先修复 pip
python3 -m ensurepip --upgrade

# 3️⃣ 安装依赖库
python3 -m pip install -r requirements.txt
# （Windows 用户可将以上命令中的 python3 替换为 python）

# 4️⃣ 启动应用
streamlit run src/physio_asst/streamlit_app/app.py

# 5️⃣ 浏览器访问（若未自动打开）
# http://localhost:8501

