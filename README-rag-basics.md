# RAG Basics (No Framework)

## What it does
A RAG system built without any framework that takes a document, divides it into chunks, stores them in a vector database, finds the most relevant chunks based on a question, and passes them to Groq as context to generate a final answer.

## How it works
1. Load a document
2. Slice it into chunks using a for loop
3. Store chunks in ChromaDB
4. Query ChromaDB with a question — returns 2 most relevant chunks
5. Join the chunks into one string
6. Send the context + question to Groq and get the answer

## Requirements
- groq
- chromadb

## Setup
1. Install dependencies: `pip install groq chromadb`
2. Set API key: `$env:GROQ_API_KEY="your_key"`
3. Run: `python rag_basics.py`
