#!/bin/bash
# Setup Script for Gemini API Key

echo "=================================="
echo "Sales Insight Automator - Setup"
echo "=================================="
echo ""

# Step 1: Get Gemini API Key
echo "📋 Step 1: Get Gemini API Key"
echo "=================================="
echo ""
echo "1. Open: https://aistudio.google.com"
echo "2. Click 'Get API Key' button"
echo "3. Create new API key for 'Sales Insight Automator'"
echo "4. Copy the key"
echo ""
read -p "Paste your Gemini API key here: " GEMINI_KEY

if [ -z "$GEMINI_KEY" ]; then
    echo "❌ API key is empty!"
    exit 1
fi

# Step 2: Update .env file
echo ""
echo "📝 Step 2: Updating .env file..."
sed -i "s/GEMINI_API_KEY=.*/GEMINI_API_KEY=$GEMINI_KEY/" .env
echo "✓ .env updated with Gemini API key"

# Step 3: Test the configuration
echo ""
echo "🧪 Step 3: Testing configuration..."
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if api_key:
    print('✓ Gemini API Key found')
    print('  Key starts with:', api_key[:10] + '...')
else:
    print('❌ Gemini API Key not found')
    exit(1)
" && echo "✓ Configuration validated"

# Step 4: Restart backend
echo ""
echo "🚀 Step 4: Restarting backend server..."
echo "Backend will restart automatically with hot reload"
echo ""
echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "Your app is now ready to:"
echo "1. Process CSV files locally"
echo "2. Generate AI summaries"
echo "3. Deploy to production"
echo ""
echo "Next: Visit http://localhost:3000 to test"
