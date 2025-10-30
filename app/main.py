from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(
    title="FastAPI 模板项目",
    description="这是一个 FastAPI 项目模板，展示了项目结构和基本用法",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "欢迎使用 FastAPI 模板项目！"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}