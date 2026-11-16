from fastapi import APIRouter

from app.models.chat_models import (
    ChatRequest
)

from app.services.ai_service import (
    AIService
)

router = APIRouter()


@router.post("/chat")
async def chat(
    data: ChatRequest
):
    reply = (
        await AIService.chat(
            data.session_id,
            data.message
        )
    )

    return {
        "reply": reply
    }
