

```markdown
# 🩺 Medical Image Analyzer using GPT-4o

This project is a Streamlit-based web application that allows users to upload medical images (like X-rays) and receive AI-generated structured medical reports using OpenAI's **GPT-4o** model. Additionally, it provides a simplified **ELI5 (Explain Like I'm 5)** explanation for non-technical users.

---

## 🚀 Features
- 📤 Upload medical images (JPG, PNG)
- 📝 Get structured medical analysis report from GPT-4o
- 🧒 Simplified ELI5 explanation for layman understanding
- 🔐 Secure API key handling (.env or Streamlit Secrets)
- 🎨 Clean & responsive UI using Streamlit

---

## 🖼️ Demo Screenshots

### 🔍 Image Upload & Analysis View



### 📊 Medical Report with ELI5 Explanation

---

## 🗂️ Project Structure
```

Medical\_app/
├── app.py              # Streamlit App code
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env, **pycache**, etc.
├── .env.template       # API key example template
├── screenshots/        # Screenshots for documentation
└── README.md           # This file

````

---

## 🛠️ Local Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/medical-image-analyzer.git
cd medical-image-analyzer
````

### 2️⃣ Setup Conda Environment

```bash
conda create -n Medical_app python=3.9 -y
conda activate Medical_app
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure OpenAI API Key

* Create a `.env` file in root:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

* Open browser: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deployment Instructions

### ✅ For Streamlit Community Cloud

* Push repo to GitHub.
* Add `OPENAI_API_KEY` in Streamlit Secrets.
* App will run automatically.

### ✅ For Render.com / Docker

* Use environment variables.
* Run using Dockerfile if containerized.

---

## 🔒 Security Best Practices

* `.env` is added to `.gitignore` (never pushed).
* Secrets are loaded via env variables or Streamlit Secrets.
* No hardcoding sensitive info in code.

---

## 📝 Requirements

* Python 3.9
* Streamlit
* OpenAI Python SDK
* python-dotenv

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

* [OpenAI GPT-4o](https://platform.openai.com/docs/guides/vision)
* [Streamlit](https://streamlit.io/)

```

---
