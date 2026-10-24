from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("syllabus.pdf")
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