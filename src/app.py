from fastapi import APIRouter, FastAPI

from src.todo.routes.todo import router as todo_router

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(todo_router, prefix="/todo")

app.include_router(v1_router)
