from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = "llama3.2:1b")

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful python instructor"),
    ("human","Explain {topic} with a simple example")
])

chain = prompt | model |  StrOutputParser()

response = chain.invoke({"topic" : "frozenset"})

print("Type:", type(response))
print("Is str:", isinstance(response, str))
print("Class module:", type(response).__module__)
print("Class name:", type(response).__name__)
print("String representation:", repr(response))
print("Length:", len(response))
print("First 50 characters:", response[:50])