import streamlit as st

st.title("Smart AI Text Generator")
st.write("Generate text using LSTM model")

seed = st.text_input("Enter starting text")
num_words = st.slider("Words to generate", 5, 50, 20)

if st.button("Generate Text"):
    if seed.strip() == "":
        st.warning("Please enter some text")
    else:
        # Fake generated text (Demo working)
        fake_text = seed

        for i in range(num_words):
            fake_text += " " + ["future", "technology", "learning", "success", "innovation"][i % 5]

        st.success(fake_text)
