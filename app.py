import streamlit as st
import base64
import os
import tempfile
from dotenv import load_dotenv
from openai import OpenAI

# === Page Config ===
st.set_page_config(page_title="Medical Image Analyzer", page_icon="🩺", layout="centered")

# === Custom CSS Styling ===
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stRadio>div>label {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# === Load .env Variables ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# === Initialize OpenAI Client ===
client = OpenAI(api_key=api_key)

# === Prompt Template ===
sample_prompt = """You’re a medical expert.

You'll get medical images.

You must analyze them in a structured report.

Always give a disclaimer: 'Consult with a doctor before making decisions'.

If unclear, say 'Unable to determine based on image'."""

# === Encode Image to Base64 ===
def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# === GPT-4o Vision Analysis ===
def call_gpt4_for_analysis(filename: str):
    base64_image = encode_image(filename)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": sample_prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "high"
                    }
                }
            ]
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1500
    )

    return response.choices[0].message.content

# === Simplify Response (ELI5) ===
def chat_eli(text):
    eli5_prompt = f"Explain this like I'm 5 years old:\n\n{text}"

    messages = [
        {
            "role": "user",
            "content": eli5_prompt
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000
    )

    return response.choices[0].message.content

# === Main App ===
def main():
    st.title("🩺 Medical Image Analyzer using GPT-4o")

    with st.expander("ℹ️ About this App"):
        st.markdown("""
        This app allows you to upload a **medical image** and receive an expert-level analysis using OpenAI's **GPT-4o**.
        - Upload an image (X-ray, MRI, etc.)
        - Get a structured medical report
        - Simplify the explanation (ELI5 Mode)
        """)

    st.divider()

    uploaded_file = st.file_uploader("📤 Upload a medical image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(uploaded_file, caption="📸 Uploaded Image", use_column_width=True)
        st.success("✅ Image uploaded successfully!")

        # Save temp file for analysis
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            temp_file_path = tmp_file.name

        if st.button("🔎 Analyze Image"):
            with st.spinner("Analyzing with GPT-4o... Please wait ⏳"):
                result = call_gpt4_for_analysis(temp_file_path)
                st.session_state['result'] = result
                st.success("✅ Analysis Complete!")

            os.unlink(temp_file_path)  # Cleanup temp file

    # Display Result
    if 'result' in st.session_state and st.session_state['result']:
        st.markdown("### 📝 GPT-4o Medical Analysis Report")
        st.markdown(st.session_state['result'], unsafe_allow_html=True)

        st.divider()

        st.info("Would you like a simpler explanation? (ELI5 Mode)")
        if st.radio("🧒 Simplify this like I'm 5?", ("No", "Yes")) == "Yes":
            with st.spinner("Simplifying explanation..."):
                simplified = chat_eli(st.session_state['result'])
                st.markdown("### 🧒 ELI5 Explanation")
                st.markdown(simplified, unsafe_allow_html=True)

# === Run App ===
if __name__ == "__main__":
    main()
