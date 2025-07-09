from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import sys
import os

# Ensure src package is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.agent import SupportAgent

# Initialize FastAPI app and AI agent
app = FastAPI()
agent = SupportAgent()

# Pydantic request model
class QueryRequest(BaseModel):
    query: str

# Pydantic response model
class QueryResponse(BaseModel):
    response: str
    confidence: float

# Root health check route
@app.get("/")
def read_root():
    return {"message": "🚀 Technical Support AI Backend is running!"}

# Support AI query endpoint
@app.post("/support", response_model=QueryResponse)
async def get_support(req: QueryRequest):
    print(f"📥 Received query: {req.query}")
    response, confidence = await agent.process_query(req.query)
    print(f"✅ Responding with: {response}, confidence: {confidence}")
    return QueryResponse(response=response, confidence=confidence)




# Entry point for standalone run (optional)
if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
