from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

path = Path("document_loader/india.pdf")

loader = PyPDFLoader(str(path))
docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)