Echo-Soul (回响之魂)
让思念跨越时空，用 AI 重塑亲人的声音与陪伴。
Echo-Soul 是一个基于本地部署的 AI 语音陪伴系统。它利用大语言模型 (LLM) 进行思维生成，结合先进的 TTS 技术 (MOSS-TTS-Nano) 实现语音合成，并支持音色克隆，旨在打造一个可以像亲人一样交流的数字生命。

✨ 核心功能
🧠 智能对话: 基于 Ollama (Qwen2.5) 的本地大模型，确保数据隐私安全。
🗣️ 语音合成: 集成 MOSS-TTS-Nano，支持高质量中文语音生成。
🎨 音色克隆 (规划中): 支持上传亲人语音样本，复刻专属音色。
💾 内存流式传输: 音频实时生成与播放，不占用硬盘存储空间。
🛠️ 技术栈
后端: Python 3.9, FastAPI
模型: Ollama (Qwen2.5), MOSS-TTS-Nano
架构: RESTful API + Microservices
🚀 快速开始
1. 环境准备
安装 Python 3.9
安装 Ollama 并下载模型: ollama pull qwen2.5:7b
克隆本仓库
2. 配置后端
cd serverpython -m venv venv.\venv\Scripts\activatepip install -r requirements.txt
3. 放置 TTS 引擎
将 MOSS-TTS-Nano 项目放入 server/lib/ 目录下。

4. 启动服务
运行 server/start_all.bat 即可一键启动所有服务。

📁 项目结构
text

Echo-Soul/
├── server/           # 后端服务
│   ├── app/          # 核心代码
│   ├── lib/          # TTS 引擎库存放处
│   └── data/         # 数据存储
└── client/           # 前端 (开发中)
📜 许可证
MIT License

🙏 致谢
Ollama
MOSS-TTS-Nano