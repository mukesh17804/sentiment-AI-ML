# Voice + Text Sentiment Analysis Using AI

This project was developed during my **Internship at MicroIT (Batch 21)** as part of my hands-on learning journey into AI, NLP, and real-time user interaction. It demonstrates how artificial intelligence can interpret human emotions from both **typed** and **spoken input**.

## 🔍 Project Overview

This application allows users to input text or use their voice to express a sentence. It then analyzes the emotional sentiment—**Positive**, **Negative**, or **Neutral**—using advanced Natural Language Processing techniques and deep learning.

Built using **Streamlit**, the app features a clean and responsive UI and offers both **speech-to-text conversion** and **real-time sentiment prediction** using a Transformer-based model from Hugging Face.

## ✅ Features

- **Dual Input Modes**: Choose between text input or voice recording.
- **Speech-to-Text Conversion**: Real-time transcription of your voice using Google's SpeechRecognition API.
- **AI-Based Sentiment Analysis**: Powered by a fine-tuned DistilBERT model from Hugging Face.
- **Confidence Score**: Displays model certainty for transparency.
- **Responsive Web App**: Streamlit-based frontend for user-friendly interaction.

## 🧠 Technologies Used

- Python 3.x
- Hugging Face Transformers
- DistilBERT (`distilbert-base-uncased-finetuned-sst-2-english`)
- Streamlit
- PyTorch
- SpeechRecognition
- PyAudio

## 🚀 How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-text-sentiment-analysis.git
cd voice-text-sentiment-analysis
