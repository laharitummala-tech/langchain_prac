from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("syllabus.pdf")
documents = loader.load()
print("total_pages",len(documents))

for i,doc in enumerate(documents):
    text = doc.page_content

    print(f"page {i+1}")
    print(f"characters {len(text)}")
    print(f"Metadata {doc.metadata}")
    print("Preview",text[:250])
