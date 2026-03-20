import streamlit as st
import pickle

import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
stem = PorterStemmer()

# Load YOUR trained model & vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# SAME cleaning function from your notebook
def clean_text(text):
    review = re.sub('[^a-zA-Z0-9]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [
        stem.stem(word)
        for word in review
        if word not in stopwords.words('english')
    ]
    return ' '.join(review)

# Streamlit UI
st.set_page_config(
    page_title="Spam Email Detection", 
    page_icon="📧"
    )

st.title("📧 Spam Email Detection using NLP")
st.write("Enter a message to check whether it is **Spam** or **Not Spam**.")

user_input = st.text_area("✉️ Enter your message")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)

        if prediction[0] == 1:
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is NOT SPAM")