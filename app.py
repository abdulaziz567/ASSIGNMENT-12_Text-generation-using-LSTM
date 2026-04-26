import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from utils import generate_text

model = load_model("model.h5")
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
max_seq_len = pickle.load(open("max_len.pkl", "rb"))

st.title("Smart AI Text Generator")
st.write("Generate realistic text using LSTM model")

seed = st.text_input("Enter starting text")
num_words = st.slider("Words to generate", 5, 50, 20)

if st.button("Generate Text"):
    result = generate_text(seed, num_words, model, tokenizer, max_seq_len)
    st.success(result)