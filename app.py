import streamlit as st
import numpy as np

# Try loading model
try:
    from tensorflow.keras.models import load_model
    import pickle
    from utils import generate_text

    model = load_model("model.h5")
    tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
    max_seq_len = pickle.load(open("max_len.pkl", "rb"))

    model_loaded = True
except:
    model_loaded = False

st.title("Smart AI Text Generator")
st.write("Generate text using LSTM model")

seed = st.text_input("Enter starting text")
num_words = st.slider("Words to generate", 5, 50, 20)

if st.button("Generate Text"):
    if model_loaded:
        result = generate_text(seed, num_words, model, tokenizer, max_seq_len)
        st.success(result)
    else:
        st.warning("⚠️ Model not loaded (Demo mode)")
