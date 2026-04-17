@echo off
echo ==========================================
echo      Echo-Soul System Starting...
echo ==========================================

:: 设置当前目录为脚本所在目录
cd /d "%~dp0"

:: 1. 设置 MOSS 所需的环境变量 (来自你的 start_moss.bat)
echo [Setup] Setting Environment Variables...
set HF_ENDPOINT=https://hf-mirror.com
set HF_HOME=D:\hf_cache

:: 2. 启动 MOSS-TTS 服务
:: 我们直接在这里启动 python app.py，不再依赖外部的 start_moss.bat
echo [1/2] Starting MOSS-TTS Engine (Internal)...
start "MOSS-TTS-Service" cmd /k "cd lib\MOSS-TTS-Nano && conda activate moss_tts && python app.py"

:: 3. 等待 MOSS 加载模型 (MOSS 加载较慢，设为 20 秒)
echo Waiting for MOSS to initialize (20 seconds)...
timeout /t 20 /nobreak

:: 4. 启动 Echo-Soul 主服务
echo [2/2] Starting Echo-Soul Main Server...
call venv\Scripts\activate
uvicorn app.main:app --host 0.0.0.0 --port 8000

echo ==========================================
echo Service Stopped.
pause