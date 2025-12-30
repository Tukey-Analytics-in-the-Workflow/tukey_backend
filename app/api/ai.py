from fastapi import APIRouter
from app.schemas.ai import AIQuery
from app.services.llm import ask_llm

router = APIRouter()

@router.post("/decision")
def ai_decision(query: AIQuery):
    response = ask_llm(query.dict())
    return response
