from groq import Groq
import chromadb
client = chromadb.Client()
collection = client.create_collection("python_document")
document = """
Python is a high-level programming language known for its simplicity and readability.
It was created by Guido van Rossum and first released in 1991.
Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.
It has a large standard library and an active community that contributes thousands of third-party packages.
Python is widely used in web development, data science, automation, and artificial intelligence.
Many companies like Google, Netflix, and Instagram use Python in their technology stack.
"""
chunks = []
for i in range(0,len(document),100):
    chunks.append(document[i:i+100])
collection.add(
    documents = chunks,
ids=["ïd1","id2","id3","id4","id5","id6"]
)
question = collection.query(
query_texts=["what technology stacks google and insta use"],
n_results=2
)
context = " ".join(question["documents"][0])
question_text = "What technology stacks do Google and Instagram use?"
prompt = f"Use this context to answer the question. Context: {context} Question: {question_text}"

client = Groq()
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": f"Answer using only this context: {context}"},
        {"role": "user", "content": question_text}
    ]
)
print(response.choices[0].message.content)




