from fastapi import APIRouter, HTTPException
from services.chatbot import ChatbotService

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/chat")
async def chat(message: str):
    try:
        response = chatbot_service.get_response(message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))