from langchain_groq import ChatGroq
from src.utils import load_config
from src.knowledge_base import KnowledgeBase
from src.error_detection import ErrorDetector
from src.mcp_tools import tools
import mlflow

class SupportAgent:
    def __init__(self):
        self.config = load_config()
        self.kb = KnowledgeBase()
        self.error_detector = ErrorDetector()
        self.model = ChatGroq(
            api_key=self.config['groq']['api_key'],
            model_name=self.config['llm']['model'],
            temperature=self.config['llm']['temperature']
        )

    async def process_query(self, query: str):
        retriever = self.kb.get_retriever()
        docs = retriever(query)
        context = "\n".join([f"Document {i}" for i, _ in docs])
        prompt = f"Question: {query}\nContext: {context}\nAnswer:"
        response = self.model.invoke(prompt)
        final_answer, score = self.error_detector.check_and_correct(response.content, tools)
        return final_answer, score
     
    