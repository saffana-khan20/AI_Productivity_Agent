from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b"
)

response = llm.invoke(
    "What is an AI agent? Explain in simple words."
)

print(response.content)