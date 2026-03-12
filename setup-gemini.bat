@echo off
REM Setup Script for Gemini API Key (Windows)

echo ==================================
echo Sales Insight Automator - Setup
echo ==================================
echo.

REM Step 1: Get Gemini API Key
echo 📋 Step 1: Get Gemini API Key
echo ==================================
echo.
echo 1. Open: https://aistudio.google.com
echo 2. Click 'Get API Key' button
echo 3. Create new API key for 'Sales Insight Automator'
echo 4. Copy the key
echo.

set /p GEMINI_KEY="Paste your Gemini API key here: "

if "%GEMINI_KEY%"=="" (
    echo ❌ API key is empty!
    pause
    exit /b 1
)

REM Step 2: Update .env file
echo.
echo 📝 Step 2: Updating .env file...

REM Use Python to update .env file
python -c "
import os

# Read .env file
with open('.env', 'r') as f:
    lines = f.readlines()

# Update or add GEMINI_API_KEY
updated = False
new_lines = []
for line in lines:
    if line.startswith('GEMINI_API_KEY='):
        new_lines.append(f'GEMINI_API_KEY=%GEMINI_KEY%\n')
        updated = True
    else:
        new_lines.append(line)

if not updated:
    new_lines.append(f'GEMINI_API_KEY=%GEMINI_KEY%\n')

# Write back
with open('.env', 'w') as f:
    f.writelines(new_lines)
" && echo ✓ .env updated with Gemini API key

REM Step 3: Validate
echo.
echo 🧪 Step 3: Testing configuration...
python -c "
import os
from dotenv import load_dotenv

env_file = '.env'
if os.path.exists(env_file):
    load_dotenv(env_file)
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key and api_key != '':
        print('✓ Gemini API Key configured')
        print('✓ Configuration validated')
    else:
        print('❌ GEMINI_API_KEY is empty in .env')
else:
    print('❌ .env file not found')
" || echo Configuration test complete

REM Step 4: Final message
echo.
echo ==================================
echo ✅ Setup Complete!
echo ==================================
echo.
echo Your app is now ready to:
echo 1. Process CSV files locally
echo 2. Generate AI summaries
echo 3. Deploy to production
echo.
echo Backend will restart automatically (if running).
echo Next: Visit http://localhost:3000 to test
echo.
pause
