from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("./pdf/ebook-springboot-2edicao.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=300)

chunks = splitter.split_documents(docs)

# for chunk in chunks:
#     print(chunk)
#     print("-"*30)

print(len(chunks))