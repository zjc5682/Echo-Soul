# server/app/api/v1/chat.py
from fastapi import APIRouter
from fastapi.responses import Response  # 引入 Response
from pydantic import BaseModel
from app.core.llm_engine import llm_engine
from app.core.tts_engine import tts_engine

router = APIRouter()

class ChatRequest(BaseModel):
    text: str

@router.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.text
    print(f"收到用户输入: {user_input}")
    
    # 1. LLM 生成回复
    reply_text = llm_engine.generate_response(user_input)
    print(f"LLM 回复: {reply_text}")
    
    # 2. TTS 合成语音 (获取二进制数据)
    audio_bytes = tts_engine.text_to_speech(reply_text)
    
    if audio_bytes:
        # 3. 直接返回音频流
        # 浏览器会自动识别并播放
        return Response(content=audio_bytes, media_type="audio/wav")
    else:
        # 如果失败，返回一个简单的错误提示音或文本
        return Response(content=b"Audio generation failed", media_type="text/plain")
    
@router.get("/speak")
async def speak_get(text: str):
    """
    直接在浏览器地址栏测试语音合成
    用法: http://localhost:8000/api/v1/speak?text=你好
    """
    print(f"[GET测试] 收到输入: {text}")
    
    # 1. 简单处理：直接把文本转语音 (跳过LLM，为了快速测试TTS)
    # 如果你想测试完整流程，可以把下面这行换成 llm_engine.generate_response(text)
    reply_text = text 
    
    audio_bytes = tts_engine.text_to_speech(reply_text)
    
    if audio_bytes:
        # 直接返回音频流
        return Response(content=audio_bytes, media_type="audio/wav")
    else:
        return Response(content=b"Audio generation failed", media_type="text/plain")    
