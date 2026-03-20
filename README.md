# 🧠 Natural Language Processing 

A structured, hands-on repository for learning **Natural Language Processing (NLP)** - from raw text preprocessing to word embeddings and real-world projects. Built using Python and Jupyter Notebooks.

---

## 📁 Repository Structure

```
NLP-from-Scratch/
│
├── Part-1_Text_Preprocessing/
│   ├── 01_Tokenization.ipynb
│   ├── 02_Stopwords.ipynb
│   ├── 03_Stemming.ipynb
│   └── 04_Lemmatization.ipynb
│
├── Part-2_Text_Representation/
│   ├── 05_Bag_of_Words.ipynb
│   ├── 06_One_Hot_Encoding.ipynb
│   ├── 07_Tf-Idf.ipynb
│   └── 08_N_gram.ipynb
│
├── Part-3_Word_Embedding/
│   ├── CBoW.ipynb
│   ├── Skip-Gram.ipynb
│   └── Word2Vec.ipynb
│
├── NLP_Projects/
│   ├── Spam_Email_Detection/
│   │   └── spam_email_detection.ipynb
│   ├── Fake_News_Detection/
│   │   └── fake_news_detection.ipynb
│   └── ... (more projects coming soon)
│
├── requirements.txt
└── README.md
```

---

## 📚 Contents Overview

### 🔹 Part 1 — Text Preprocessing
Fundamental steps to clean and prepare raw text data before feeding it into any NLP model.

| Notebook | Description |
|----------|-------------|
| `01_Tokenization.ipynb` | Splitting text into words or sentences (tokens) |
| `02_Stopwords.ipynb` | Removing common words that carry little meaning (e.g., "the", "is") |
| `03_Stemming.ipynb` | Reducing words to their root form (e.g., "running" → "run") |
| `04_Lemmatization.ipynb` | Smarter root-form reduction using vocabulary & grammar rules |

---

### 🔹 Part 2 — Text Representation
Techniques to convert text into numerical formats that machine learning models can understand.

| Notebook | Description |
|----------|-------------|
| `05_Bag_of_Words.ipynb` | Representing text as word frequency counts |
| `06_One_Hot_Encoding.ipynb` | Binary vector representation of words |
| `07_Tf-Idf.ipynb` | Weighting words by importance across documents |
| `08_N_gram.ipynb` | Capturing context using sequences of N words |

---

### 🔹 Part 3 — Word Embeddings
Dense vector representations that capture semantic meaning and relationships between words.

| Notebook | Description |
|----------|-------------|
| `CBoW.ipynb` | Continuous Bag of Words — predict a word from its context |
| `Skip-Gram.ipynb` | Predict surrounding context words from a target word |
| `Word2Vec.ipynb` | Full Word2Vec implementation using Gensim |

---

### 🔹 NLP Projects
End-to-end NLP projects applying the concepts learned above to real-world problems.

| Project | Description | Status |
|---------|-------------|--------|
| 📧 `Spam_Email_Detection` | Classifies emails as **spam or not spam** using NLP + ML | ✅ Complete |
| 📰 `Fake_News_Detection` | Identifies whether a news article is **real or fake** | ✅ Complete |
| 🔜 More projects... | Sentiment Analysis, NER, Text Summarization, and more | 🚧 Coming Soon |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Purvijain1234/Natural-Language-Processing-by-Purvi-Jain.git
cd Natural-Language-Processing-by-Purvi-Jain
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Mac/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 🛠️ Requirements

Key libraries used across this repo:

```
nltk
scikit-learn
gensim
pandas
numpy
matplotlib
seaborn
jupyter
```

> Install all at once: `pip install -r requirements.txt`

---

## 🗺️ Learning Path

If you're new to NLP, follow this recommended order:

```
Part 1 (Preprocessing) → Part 2 (Representation) → Part 3 (Embeddings) → NLP Projects
```

Each part builds on the previous one, giving you a solid foundation before diving into real projects.

---

## 🚀 Future Plans

- [ ] Part-4: Sequence Models (RNN, LSTM)
- [ ] Part-5: Transformers & Attention
- [ ] More NLP Projects (Sentiment Analysis, Named Entity Recognition, Text Summarization)
- [ ] Add datasets for all projects

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or suggestions
- Submit a pull request with improvements or new notebooks
- Star ⭐ the repo if you find it helpful!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">
  <b>Built with ❤️ for NLP learners</b><br>
  If this repo helped you, consider giving it a ⭐
</div>
