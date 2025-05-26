# 💬 Semantic Quote Retriever (RAG Style)

A semantic search application that lets you query famous quotes using natural language.  
Built using a lightweight RAG-style (Retrieval-Augmented Generation) approach with **Sentence Transformers**, **FAISS**, and **Streamlit**.

🔗 **Live App**: [semantic-quote-retriever.streamlit.app](https://semantic-quote-retriever-5sztrf7b2g4rmhug66gtlf.streamlit.app/)

---

## 🔍 Features

- Natural language search on 1,000+ quotes
- Sentence embeddings via `all-MiniLM-L6-v2`
- Fast semantic similarity search using FAISS
- Beautiful interactive UI built with Streamlit
- Deployed to [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📦 Tech Stack

- 🧠 `sentence-transformers`
- 🔎 `faiss-cpu`
- 📚 `datasets` (from Hugging Face)
- 🌐 `streamlit`


---
🎥 Demo Video
👉 [https://drive.google.com/file/d/1HNsf02ve8lADID4U8wWTl46kwLQwUswD/view?usp=sharing]

🧪 How It Works
1) Loads the Abirate/english_quotes dataset
2) Encodes quotes using all-MiniLM-L6-v2 sentence transformer
3) Builds a FAISS index on the quote embeddings
4) Takes your query → encodes it → finds top-k closest quotes
5) Displays results with author names using Streamlit
6) Notebook Link: https://colab.research.google.com/drive/1mT9PSQHZI-ORqEiZdPGqxIhJrhcJ0pdV?usp=sharing

🧠 Example Queries
Try searching with:

"motivational quotes about life"

"funny quotes by women authors"

"quotes on reading and books"

"peaceful thoughts about happiness"

   
## 🚀 Running Locally

1. **Clone this repo**

```bash
git clone https://github.com/Aswinthmani2003/semantic-quote-retriever.git
cd semantic-quote-retriever  
```
2. **Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
streamlit run app.py
```
4. Visit
```bash
http://localhost:8501
```
## Sample Output

![image](https://github.com/user-attachments/assets/b1b1dfef-eca8-4612-9e4a-0cc12da4f1ad)

