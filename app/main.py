from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.avatar_router import avatar_router
from app.api.routers.user_router import user_router
from app.api.routers.dashboard_router import dashboard_router
app = FastAPI()

#corst
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

#include routers
app.include_router(avatar_router)
app.include_router(user_router)
app.include_router(dashboard_router)
#test apis

@app.get('/test')
def test():
    return {'data': 'data from backend'}