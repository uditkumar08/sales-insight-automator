#!/bin/bash

# Sales Insight Automator - Local Setup Script
# This script sets up the entire development environment

set -e  # Exit on error

echo "🚀 Sales Insight Automator - Setup Script"
echo "=========================================="
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.11+"
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 18+"
    exit 1
fi

echo "✓ Python $(python3 --version | awk '{print $2}')"
echo "✓ Node $(node --version)"
echo ""

# Setup Backend
echo "🔧 Setting up Backend..."

cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -q -r requirements.txt

# Create .env file if not exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp ../.env.example .env
    echo "⚠️  Please edit backend/.env with your credentials:"
    echo "   - GEMINI_API_KEY: Get from https://aistudio.google.com"
    echo "   - EMAIL_USER & EMAIL_PASS: Gmail app-specific password"
fi

echo "✓ Backend setup complete"
cd ..
echo ""

# Setup Frontend
echo "🔧 Setting up Frontend..."

cd frontend

# Install dependencies
echo "Installing Node packages..."
npm install -q

# Create .env file if not exists
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
fi

echo "✓ Frontend setup complete"
cd ..
echo ""

# Summary
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "==========="
echo ""
echo "1️⃣  Configure environment variables:"
echo "   Edit backend/.env with your API keys"
echo ""
echo "2️⃣  Start backend (in new terminal):"
echo "   cd backend"
echo "   source venv/bin/activate  # or venv\\Scripts\\activate on Windows"
echo "   uvicorn app.main:app --reload"
echo ""
echo "3️⃣  Start frontend (in another terminal):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "4️⃣  Open browser:"
echo "   Frontend: http://localhost:5173"
echo "   Backend:  http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "📚 Documentation:"
echo "   - README.md: Project overview and API docs"
echo "   - DEPLOYMENT_GUIDE.md: Production deployment steps"
echo ""
