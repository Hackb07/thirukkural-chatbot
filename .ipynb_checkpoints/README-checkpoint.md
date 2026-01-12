# Thirukkural Chatbot
An AI-Powered, Article-Wise Semantic Chatbot for Classical Tamil Literature
## Project Overview

The Thirukkural Chatbot is a closed-domain AI system designed to answer user queries strictly based on Thirukkural.
It uses semantic search (FAISS) and sentence embeddings to retrieve the most relevant Kurals along with their meanings and explanations.

This project bridges classical Tamil literature and modern machine learning, making Thirukkural accessible through an interactive chat interface.

## Key Features

✅ Covers all 1330 Thirukkural verses

✅ Article-wise (Adhigaram-wise) retrieval

✅ Semantic search using FAISS

✅ Tamil + English support

✅ Streamlit-based chat UI

✅ Closed-domain (no hallucinations)

✅ Configurable number of results (up to 15 kurals)

## System Architecture
User Query
   ↓
Sentence Transformer (Embedding)
   ↓
FAISS Vector Search
   ↓
Relevant Thirukkural Retrieval
   ↓
Streamlit Chat Interface

 ## Project Structure
thirukkural_chatbot/
│
├── app.py                      # Streamlit chat UI
├── retriever.py                # FAISS-based retrieval logic
├── build_faiss_index.py        # Index creation script
├── thirukkural_chatbot_dataset.csv
├── thirukkural.faiss           # FAISS vector index
├── thirukkural.pkl             # Pickled dataset
├── requirements.txt
└── README.md

## Dataset Description

Total Verses: 1330

Columns Used:

Chapter Name (Adhigaram)

Section Name (Paal)

Verse (Tamil)

Translation (English)

Explanation

The dataset is public-domain, structured, and fully suitable for ML/NLP applications.

## Technologies Used

Python 3.9+

Streamlit – Chat UI

Sentence Transformers – Semantic embeddings

FAISS – Vector similarity search

Pandas – Dataset handling

## Installation
### 1️Clone the Repository
```git clone https://github.com/your-username/thirukkural-chatbot.git```
```cd thirukkural-chatbot```

### 2️ Install Dependencies
```pip install -r requirements.txt```

### Build the FAISS Index (One-Time Step)
```python build_faiss_index.py```


Expected output:

✅ FAISS index built successfully
🔢 Total vectors indexed: 1330

### 4 Run the Chatbot
```streamlit run app.py```


Open your browser and start chatting 🎉

## Example Queries

What does Thirukkural say about friendship?

Give kurals related to leadership

Explain a kural on honesty

Advice for good character from Thirukkural

## 🎓 Academic Relevance

This project demonstrates:

Practical application of Machine Learning

Semantic search using vector databases

Explainable AI using retrieval-based methods

Ethical AI with zero hallucination

## Suitable for:

Final-year projects

ML / NLP coursework

Research demonstrations

Cultural AI applications

## 🚀 Future Enhancements

🔹 Tamil transliteration support

🔹 Voice-based chatbot

🔹 Adhigaram-wise filters

🔹 Mobile app version

🔹 Fine-tuned Tamil language model

## 📜 License & Ethics

Thirukkural is public-domain literature

Dataset used strictly for educational and research purposes

No external or generated content outside Thirukkural is included
## 🙌 Acknowledgements

Classical Tamil literature sources

Open-source ML & NLP community

FAISS and Sentence Transformers developers

## 📧 Contact

For academic or project-related queries, feel free to reach out.