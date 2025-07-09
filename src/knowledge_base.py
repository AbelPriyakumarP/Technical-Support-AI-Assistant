from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
import numpy as np
import os
from src.embeddings import get_embeddings
from src.utils import load_config


class KnowledgeBase:
    def __init__(self):
        self.config = load_config()
        self.embeddings = get_embeddings()

    def load_documents(self):
        """
        Load all .md documents from the knowledge base directory, 
        split them into manageable chunks.
        """
        kb_path = self.config['knowledge_base']['source_directory']

        if not os.path.exists(kb_path):
            raise FileNotFoundError(f"📂 Knowledge base directory not found: {kb_path}")

        loader = DirectoryLoader(kb_path, glob="**/*.md")
        docs = loader.load()

        if not docs:
            raise ValueError(f"⚠️ No .md files found in: {kb_path}")

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return splitter.split_documents(docs)

    def build_vector_store(self):
        """
        Builds FAISS vector store from document embeddings and writes to disk.
        """
        documents = self.load_documents()
        if not documents:
            raise ValueError("⚠️ No documents found to build vector store.")

        texts = [doc.page_content for doc in documents]
        if not texts:
            raise ValueError("⚠️ Documents have no content.")

        vectors = np.array(self.embeddings.embed_documents(texts), dtype=np.float32)
        if vectors.size == 0:
            raise ValueError("⚠️ Embedding vectors could not be generated.")

        index = faiss.IndexFlatL2(vectors.shape[1])
        index.add(vectors)
        faiss.write_index(index, self.config["faiss"]["index_path"])

    def get_retriever(self):
        """
        Returns a retriever function that retrieves the top-k closest 
        vectors for a given query embedding.
        """
        if not os.path.exists(self.config['faiss']['index_path']):
            self.build_vector_store()

        index = faiss.read_index(self.config['faiss']['index_path'])

        def retriever(query: str, k=5):
            embedding = np.array([self.embeddings.embed_query(query)], dtype=np.float32)
            distances, indices = index.search(embedding, k)
            return [(indices[0][i], distances[0][i]) for i in range(k)]

        return retriever
