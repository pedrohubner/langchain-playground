import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector

load_dotenv()

for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set.")

current_dir = Path(__file__).parent
pdf_path = current_dir / "pdf/ebook-springboot-2edicao.pdf"

docs = PyPDFLoader(pdf_path).load()

splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=False).split_documents(docs)

if not splits:
    raise System_Exist(0)

enriched_split = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if not v in ("", None)}
    )
    for d in splits
]

ids = [f"doc-{i}" for i in range(len(enriched_split))]
embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True
)

store.add_documents(documents=enriched_split, ids=ids)