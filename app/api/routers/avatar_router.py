from fastapi import APIRouter, Request
from app.api.controllers.avatar_controller import AvatarController

avatar_router = APIRouter(
    prefix='/avatar'
)

@avatar_router.post('/question')
async def question(req: Request):
    question = await req.json()
    return AvatarController().get_response_for_question(question)