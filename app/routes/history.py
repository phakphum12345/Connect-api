from fastapi import APIRouter

from app.services.memory_service import (
    MemoryService
)

router = APIRouter()


@router.get(
    "/history/{session_id}"
)
async def history(
    session_id: str
):
    return (
        MemoryService.get_history(
            session_id
        )
    )


@router.get("/sessions")
async def sessions():
    return {
        "sessions":
        MemoryService.get_sessions()
    }


@router.delete(
    "/history/{session_id}"
)
async def delete_history(
    session_id: str
):
    MemoryService.delete_history(
        session_id
    )

    return {
        "success": True
    }
