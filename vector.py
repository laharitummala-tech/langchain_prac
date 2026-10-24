from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)



loader = PyPDFLoader("python_notes.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("total pages", len(documents))
print("total chunks", len(chunks))
print(chunks[0].page_content)
print(chunks[0].metadata)


vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="python_notes"
)

print("vector store created successfully")
print("Chunks indexed",len(chunks))

# retrive

results = vector_store.similarity_search(
    "What are python data types?",
    k = 3
)

for i,doc in enumerate(results,start=1):
    print(f"result {i}")
    print(doc.page_content[:500])
    print("Metadata", doc.metadata)

    