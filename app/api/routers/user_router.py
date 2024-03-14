from fastapi import APIRouter, Request
from app.api.controllers.user_controller import UserController

user_router = APIRouter(
    prefix='/user'
)

@user_router.post('/auth')
async def auth(req: Request):
    data = await req.json()
    return UserController().authentication(data)

@user_router.post('/validate_access_token')
async def valdiate(req: Request):
    data = await req.json()
    return UserController().validate_access_token(data)