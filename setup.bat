@echo off
REM Sales Insight Automator - Local Setup Script (Windows)
REM This script sets up the entire development environment

echo 🚀 Sales Insight Automator - Setup Script (Windows)
echo ================================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.11+
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Python %PYTHON_VERSION%

REM Check Node
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js not found. Please install Node.js 18+
    pause
    exit /b 1
)

for /f %%i in ('node --version') do set NODE_VERSION=%%i
echo ✓ Node %NODE_VERSION%
echo.

REM Setup Backend
echo 🔧 Setting up Backend...

cd backend

REM Create virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing Python dependencies...
pip install -q -r requirements.txt

REM Create .env file if not exists
if not exist ".env" (
    echo Creating .env file from template...
    copy ..\.env.example .env
    echo ⚠️  Please edit backend\.env with your credentials:
    echo    - GEMINI_API_KEY: Get from https://aistudio.google.com
    echo    - EMAIL_USER ^& EMAIL_PASS: Gmail app-specific password
)

echo ✓ Backend setup complete
cd ..
echo.

REM Setup Frontend
echo 🔧 Setting up Frontend...

cd frontend

REM Install dependencies
echo Installing Node packages...
call npm install -q

REM Create .env file if not exists
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
)

echo ✓ Frontend setup complete
cd ..
echo.

REM Summary
echo ✅ Setup complete!
echo.
echo Next steps:
echo ===========
echo.
echo 1️⃣  Configure environment variables:
echo    Edit backend\.env with your API keys
echo.
echo 2️⃣  Start backend ^(in new terminal^):
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn app.main:app --reload
echo.
echo 3️⃣  Start frontend ^(in another terminal^):
echo    cd frontend
echo    npm run dev
echo.
echo 4️⃣  Open browser:
echo    Frontend: http://localhost:5173
echo    Backend:  http://localhost:8000
echo    API Docs: http://localhost:8000/docs
echo.
echo 📚 Documentation:
echo    - README.md: Project overview and API docs
echo    - DEPLOYMENT_GUIDE.md: Production deployment steps
echo.
pause
