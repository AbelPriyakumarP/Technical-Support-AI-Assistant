from langchain_groq import ChatGroq
from src.utils import load_config

class ErrorDetector:
    def __init__(self):
        self.config = load_config()
        self.model = ChatGroq(api_key=self.config['groq']['api_key'],
                              model_name=self.config['llm']['model'],
                              temperature=self.config['llm']['temperature'])

    def check_and_correct(self, response, tools):
        updated_response = response
        if "python 3.10" in response:
            updated_response = response.replace("python 3.10", f"python {tools[0]('python')}")
        return updated_response, 0.95