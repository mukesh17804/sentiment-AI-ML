# voice_sentiment_app.py

import streamlit as st
from transformers import pipeline
import speech_recognition as sr

# Load sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Emoji map
emoji_map = {
    "POSITIVE": "😊",
    "NEGATIVE": "😠",
    "NEUTRAL": "😐"
}

# Function to capture voice
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "Speech Recognition service is unavailable."

# UI
st.title("🎙️ Voice + Text Sentiment Analyzer")
st.write("Type or speak a sentence to get its sentiment analyzed by AI.")

option = st.radio("Choose input method:", ["📝 Type Text", "🎤 Use Microphone"])

if option == "📝 Type Text":
    user_input = st.text_area("Enter your text:", height=150)
    if st.button("🔍 Analyze"):
        if user_input.strip():
            result = sentiment_pipeline(user_input)[0]
            st.markdown(f"{emoji_map.get(result['label'], '🤔')} **Sentiment**: {result['label']}")
            st.markdown(f"🔢 **Confidence**: {round(result['score'] * 100, 2)}%")
        else:
            st.warning("Please enter some text.")

elif option == "🎤 Use Microphone":
    if st.button("🎧 Start Listening"):
        text = get_voice_input()
        st.markdown(f"📝 **Recognized Text**: `{text}`")
        if "Sorry" not in text:
            result = sentiment_pipeline(text)[0]
            st.markdown(f"{emoji_map.get(result['label'], '🤔')} **Sentiment**: {result['label']}")
            st.markdown(f"🔢 **Confidence**: {round(result['score'] * 100, 2)}%")
