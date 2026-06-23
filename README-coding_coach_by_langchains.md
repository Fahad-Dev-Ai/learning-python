# Coding Coach Chatbot (LangChain)

## What it does
A coding coach chatbot that explains Python concepts in simple language using LangChain and Groq.

## How it works
1. User enters a question
2. LangChain formats it into a prompt template
3. Groq LLM generates a response
4. Conversation history is stored and printed on exit

## Requirements
- langchain-groq
- langchain-core

## Setup
1. Install dependencies: `pip install langchain-groq langchain-core`
2. Set API key: `$env:GROQ_API_KEY="your_key"`
3. Run: `python coding_coach_by_langchain.py`
