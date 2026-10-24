from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# create the model
model = ChatOllama(model = "llama3.2:1b")

# prepare the messages
messages = [
    SystemMessage(content="""
You are a Java-only tutor.

Rules:
1. Answer questions about Java only.
2. If the question is about Python, C++, JavaScript,
   or any other non-Java language, do not explain it.
3. For non-Java questions, reply with exactly:
   "Sorry, I can only answer questions about Java."
"""),
    HumanMessage(content="who is the prime minister of india?")
]

response = model.invoke(messages)

print(response.type)

# print(dir(model))