import os

from dotenv import load_dotenv
from openai import OpenAI

from app.services.memory_service import (
    MemoryService
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)

MODEL = os.getenv(
    "MODEL_NAME",
    "gpt-4o-mini"
)


class AIService:

    @staticmethod
    async def chat(
        session_id,
        message
    ):

        history = (
            MemoryService.get_history(
                session_id
            )
        )

        messages = [
            {
                "role": "system",
                "content":
                """
                You are ISH.
                Helpful AI Assistant.
                """
            }
        ]

        messages.extend(
            history
        )

        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        response = (
            client.chat.completions.create(
                model=MODEL,
                messages=messages
            )
        )

        reply = (
            response.choices[0]
            .message.content
        )

        MemoryService.save_message(
            session_id,
            "user",
            message
        )

        MemoryService.save_message(
            session_id,
            "assistant",
            reply
        )

        return reply
