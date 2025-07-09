from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("./knowledge_base", glob="**/*.md")
docs = loader.load()
print(f"Found {len(docs)} documents.")
