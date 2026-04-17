from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1 import chat

# 创建 FastAPI 应用
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# 1. 配置跨域 (允许 Vue 前端访问)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议改为具体的前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. 挂载静态文件目录
# 这样前端可以通过 http://localhost:8000/static/audio/xxx.wav 访问音频
app.mount("/static/audio", StaticFiles(directory=settings.AUDIO_CACHE_DIR), name="audio")

# 3. 注册路由
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])

# 根路径测试
@app.get("/")
def read_root():
    return {"message": "Echo-Soul 后端服务运行中", "docs": "/docs"}

# 启动提示
@app.on_event("startup")
async def startup_event():
    print(f"服务启动: {settings.PROJECT_NAME}")
    print(f"音频缓存目录: {settings.AUDIO_CACHE_DIR}")