from fastapi import APIRouter, Request
from app.api.controllers.dashboard_controller import DashboardController

dashboard_router = APIRouter(
    prefix='/dashboard'
)

@dashboard_router.get('/comments_users')
def auth():
    return DashboardController().comments_users()