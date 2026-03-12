# 🚀 Complete Setup & Deployment Guide

## Step 1: Get Your Gemini API Key (5 minutes)

### Windows:
```bash
setup-gemini.bat
```

### macOS/Linux:
```bash
bash setup-gemini.sh
```

Or manually:
1. **Go to:** https://aistudio.google.com
2. **Click:** "Get API Key"
3. **Create new:** "Sales Insight Automator"
4. **Copy the key**
5. **Edit:** `backend/.env`
   ```
   GEMINI_API_KEY=your_key_here
   ```

## Step 2: Run Locally

**Terminal 1 - Backend:**
```bash
cd backend
..\\.venv\\Scripts\\python.exe -m uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Visit:** http://localhost:3000

## Step 3: Deploy to Production (Anyone Can Access)

### Option A: Deploy Backend to Render (Free)

**Your backend will be at:** `https://your-app-backend.onrender.com`
- Can be accessed from **anywhere** in the world
- Automatically scales
- No credit card for free tier

**Steps:**
1. Go to https://render.com
2. Connect GitHub repository
3. Create Web Service
4. Set environment variables:
   ```
   GEMINI_API_KEY=your_key_from_aistudio
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   FRONTEND_URL=https://your-frontend.vercel.app
   ENVIRONMENT=production
   ```
5. Deploy - Done!

### Option B: Deploy Frontend to Vercel (Free)

**Your frontend will be at:** `https://your-app.vercel.app`
- Can be accessed from **anywhere** in the world
- Auto-deploys on push to GitHub
- Global CDN

**Steps:**
1. Go to https://vercel.com
2. Connect GitHub repository
3. Select `frontend` folder
4. Set environment:
   ```
   VITE_API_URL=https://your-app-backend.onrender.com
   ```
5. Deploy - Done!

## Step 4: Share Your App

Once deployed:
- **Backend API:** `https://your-app-backend.onrender.com`
- **Frontend URL:** `https://your-app.vercel.app`

**Anyone can now:**
- Open your frontend URL
- Upload CSV files
- Get AI summaries
- Receive emails

## Production Checklist

### Security
- ✅ API keys stored in environment variables (never in code)
- ✅ CORS configured for multiple origins
- ✅ HTTPS enforced on deployment
- ✅ Input validation on all endpoints

### Performance
- ✅ Frontend code optimized for production build
- ✅ Backend handles concurrent requests
- ✅ Email sent asynchronously
- ✅ Health check endpoints available

### Monitoring
- ✅ Backend logs all requests
- ✅ Error handling for API failures
- ✅ Configuration logging on startup
- ✅ Health endpoint for monitoring

### Testing
- ✅ Test with different CSV formats
- ✅ Verify email delivery works
- ✅ Check CORS from different origins
- ✅ Monitor backend logs for errors

## Accessible From Anywhere

Your app works:
- ✅ On localhost
- ✅ Deployed to Render
- ✅ Deployed to Vercel
- ✅ From mobile devices
- ✅ From any browser, any location
- ✅ Multiple concurrent users

## Environment Variables

### Backend (.env or Render settings)
```
GEMINI_API_KEY=sk_xxx...
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
FRONTEND_URL=https://your-frontend.vercel.app
ENVIRONMENT=production
```

### Frontend (.env.production or Vercel settings)
```
VITE_API_URL=https://your-app-backend.onrender.com
```

## Making It Public & Usable

Once deployed:

1. **Share the frontend URL** in Slack, email, etc.
2. **Anyone can visit:** `https://your-app.vercel.app`
3. **They can upload CSVs**
4. **Get AI-generated summaries**
5. **Check their email**

No login, no installation, just **click and use!**

## Troubleshooting

### "API connection failed"
- Check `VITE_API_URL` in Vercel environment
- Verify backend is running: `https://your-api.onrender.com/health`

### "Email not sending"
- Verify Gmail app password (not regular password)
- Check EMAIL_USER and EMAIL_PASS in environment

### "Gemini API error"
- Verify API key is correct from aistudio.google.com
- Check API quota not exceeded
- Review API key permissions

## Next Steps

1. Run `setup-gemini.bat` or `setup-gemini.sh`
2. Start local servers
3. Test on http://localhost:3000
4. Deploy to Render & Vercel
5. Share the frontend URL with anyone
6. Monitor in Render/Vercel dashboards

---

**Questions?** Check the main README.md or DEPLOYMENT_GUIDE.md
