import httpx
from app.config import settings

class LLMEngine:
    def __init__(self):
        self.url = settings.OLLAMA_API_URL
        self.model = settings.OLLAMA_MODEL_NAME

    def generate_response(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False 
        }
        try:
            with httpx.Client(timeout=120.0) as client:
                response = client.post(self.url, json=payload)
                response.raise_for_status()
                result = response.json()
                return result.get("response", "抱歉，我好像走神了...")
        except Exception as e:
            print(f"Ollama 调用失败: {e}")
            return "大脑连接中断..."

llm_engine = LLMEngine()