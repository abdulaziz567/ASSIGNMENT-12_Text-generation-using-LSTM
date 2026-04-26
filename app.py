import streamlit as st

# Page config
st.set_page_config(page_title="Neural Text Generator", page_icon="✨", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #00f5d4;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        color: #cfcfcf;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #00f5d4;
        color: black;
        font-size: 16px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="title">✨ Neural Text Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate text using LSTM-based AI concept</div>', unsafe_allow_html=True)

# Input Box
seed = st.text_input("📝 Enter your starting text")

# Slider
num_words = st.slider("🔢 Number of words to generate", 5, 50, 20)

# Generate Button
if st.button("🚀 Generate Text"):
    if seed.strip() == "":
        st.warning("⚠️ Please enter some text first!")
    else:
        # Fake generated text (Demo working)
        fake_text = seed

        words = ["future", "technology", "learning", "success", "innovation"]
        for i in range(num_words):
            fake_text += " " + words[i % len(words)]

        st.success("✅ Generated Text:")
        st.write(fake_text)

# Footer
st.markdown("---")
st.markdown("👨‍💻 Developed by Abdul Aziz")
