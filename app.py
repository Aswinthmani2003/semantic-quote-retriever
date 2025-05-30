import streamlit as st
from sentence_transformers import SentenceTransformer
from datasets import load_dataset
import numpy as np
import faiss
import torch

model = SentenceTransformer("all-MiniLM-L6-v2")


st.title("💬 Semantic Quote Search")

# Load dataset from Hugging Face
dataset = load_dataset("Abirate/english_quotes", split="train")
dataset = dataset.filter(lambda x: x["quote"] and x["author"])
dataset = dataset.shuffle(seed=42).select(range(1000))

quotes = dataset["quote"]
authors = dataset["author"]

# Load model and encode
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(quotes)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# UI
query = st.text_input("🔍 Enter your query:")
if query:
    query_emb = model.encode([query])
    _, indices = index.search(np.array(query_emb), 5)
    for i in indices[0]:
        st.markdown(f"> *{quotes[i]}*  \n\n— **{authors[i]}**")
        st.markdown("---")
