import httpx
import uuid
import os
import base64
from app.config import settings

class TTSEngine:
    def __init__(self):
        self.url = "http://localhost:18083/api/generate" 
        self.demo_id = settings.MOSS_DEMO_ID
        print(f"TTS 引擎初始化完成，目标地址: {self.url}，默认音色: {self.demo_id}")

    def text_to_speech(self, text: str) -> bytes:
        """
        调用 MOSS 服务生成语音
        返回: 音频的二进制数据
        """
        payload = {
            "text": text,
            "demo_id": self.demo_id
        }
        
        try:
            with httpx.Client(timeout=120.0) as client:
                response = client.post(self.url, data=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    audio_base64 = result.get("audio_base64")
                    
                    if audio_base64:
                        # 直接解码成二进制数据，不保存文件
                        audio_bytes = base64.b64decode(audio_base64)
                        print(f"语音合成成功 (内存模式，大小: {len(audio_bytes)} bytes)")
                        return audio_bytes
                    else:
                        print(f"错误：响应中未包含 audio_base64")
                        return None
                else:
                    print(f"MOSS 服务返回错误: {response.status_code} - {response.text}")
                    return None
                    
        except httpx.ConnectError:
            print("错误：无法连接到 MOSS-TTS 服务")
            return None
        except Exception as e:
            print(f"语音合成失败: {e}")
            return None

tts_engine = TTSEngine()