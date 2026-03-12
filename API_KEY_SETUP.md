# 🔑 Getting Your Gemini API Key - Visual Guide

## 5-Minute Setup

### Option 1: Automated Script (Easiest)

**Windows:**
```powershell
# Just run this command:
setup-gemini.bat
```

**macOS/Linux:**
```bash
# Just run this command:
bash setup-gemini.sh
```

Then follow the prompts to paste your key.

---

## Option 2: Manual Setup (2 minutes)

### Step 1: Get API Key from Google

1. **Open:** https://aistudio.google.com

2. **Click "Get API Key"** button in top right

   ![image: Shows "Get API Key" button on Google AI Studio]

3. **Click "Create API key"** in new project

   ![image: Shows "Create API key" dropdown]

4. **Copy the displayed key**

   ![image: Shows API key that looks like: sk_xxxxxxxxxxxxx]

### Step 2: Add to Your .env File

**Windows (using Notepad):**
```powershell
# Open the file:
notepad backend\.env
```

**Mac/Linux:**
```bash
# Open the file:
nano backend/.env
# or
vim backend/.env
```

**Edit the line:**
```env
GEMINI_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxx
```

Save and close.

### Step 3: Backend Restarts Automatically

Your backend will:
1. Detect the new key
2. Reload automatically (hot reload enabled)
3. Start accepting AI requests

---

## Testing It Works

```bash
# In any terminal:
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","version":"1.0.0","gemini_configured":true}
```

If `gemini_configured` is `true` → ✅ Success!

---

## Your Keys Are Safe

```
.env file:
- ✅ Contains your API keys
- ✅ In .gitignore (never goes to GitHub)
- ✅ Only on your computer
- ✅ Secret by default
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Setup script won't run | Right-click → Run as Administrator |
| "API key invalid" | Copy key again from aistudio.google.com (exact copy) |
| Backend doesn't reload | Restart terminal or restart backend manually |
| Can't find .env file | It's in `backend/` folder, named `.env` (starts with dot) |

---

## What Happens After

Once configured:

✅ **Local (localhost):**
- Upload CSV → Get summary in ~5 seconds
- Summary sent to your email

✅ **Production (Render/Vercel):**
- Anyone with your Vercel URL can upload
- AI processes and sends anywhere
- Works for 100+ people simultaneously

---

## Security Notes

- 🔐 API key only in `.env` file (never in code)
- 🔐 Never share your `.env` file
- 🔐 `.env` is in `.gitignore` (safe from git)
- 🔐 Each environment has its own key (local, staging, prod)

---

## Free Tier Info

**Gemini API:**
- ✅ Free tier available
- ✅ 60 requests per minute limit
- ✅ Enough for testing
- ✅ Can upgrade anytime

**Render & Vercel:**
- ✅ Both have free tiers
- ✅ Perfect for starting out
- ✅ No credit card required initially

---

## Next Steps After Adding Key

1. ✅ Backend will auto-reload (check terminal)
2. ✅ Visit http://localhost:3000
3. ✅ Upload test CSV
4. ✅ Check your email for summary
5. ✅ Deploy to production when ready!

---

**That's it! Your API is ready.** 🚀
