import os
from pathlib import Path

# 获取 server 目录的绝对路径
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings:
    # 项目基础配置
    PROJECT_NAME = "Echo-Soul Server"
    VERSION = "0.1.0"
    
    # Ollama 配置
    OLLAMA_API_URL = "http://localhost:11434/api/generate"
    OLLAMA_MODEL_NAME = "qwen2.5:7b"
    
    # MOSS-TTS 配置
    MOSS_API_URL = "http://localhost:18083/api/generate"
    
    # === 新增配置 ===
    # MOSS 默认音色 ID (先设为 "1"，如果报错再改)
    MOSS_DEMO_ID = "demo-3"
    
    # 音频缓存目录
    AUDIO_CACHE_DIR = str(BASE_DIR / "data" / "audio_cache")
    
    # 设备配置
    DEVICE = "cpu"

settings = Settings()

# 启动时自动创建缓存目录
os.makedirs(settings.AUDIO_CACHE_DIR, exist_ok=True)