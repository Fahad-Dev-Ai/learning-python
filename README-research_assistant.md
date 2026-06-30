# Research Assistant Agent

## What it does
An AI agent that takes any research question, searches the web for current information, and summarizes the findings into clean, readable bullet points. Built using LangGraph with autonomous tool selection.

## How it works
1. User asks a research question
2. Agent decides to search the web using DuckDuckGo
3. Raw search results get passed to a custom summarizer tool
4. Summarizer tool uses Groq LLM to condense results into bullet points
5. Agent returns the clean summary as the final answer

## Tools used
- DuckDuckGo Search — fetches real-time web information
- Custom Summarizer Tool — condenses raw text into bullet points using Groq

## Tech stack
- LangGraph (create_react_agent)
- Groq API (openai/gpt-oss-120b)
- LangChain tools (@tool decorator)
- DuckDuckGo Search

## Setup
1. Install: `pip install langchain-groq langchain-community langgraph duckduckgo-search ddgs`
2. Set API key: `$env:GROQ_API_KEY="your_key"`
3. Run: `python research_assistant.py`
4. Enter any research question when prompted
