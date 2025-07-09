from sentence_transformers import SentenceTransformer

class LocalEmbeddings:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim vectors

    def embed_documents(self, texts):
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_query(self, text):
        return self.model.encode([text], convert_to_numpy=True).tolist()[0]

def get_embeddings():
    return LocalEmbeddings()
