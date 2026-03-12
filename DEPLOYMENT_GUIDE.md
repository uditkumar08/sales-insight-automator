# Deployment Guide

Complete step-by-step guide to deploy Sales Insight Automator to Render and Vercel.

## Prerequisites
- GitHub account with repository access
- Render account (render.com)
- Vercel account (vercel.com)
- Google Gemini API key (aistudio.google.com)
- Gmail account with app-specific password

## Part 1: Prepare Your Repository

### 1. Push Code to GitHub
```bash
git add .
git commit -m "feat: Add production deployment configs"
git push origin main
```

### 2. Verify .env files are ignored
```bash
# Check .gitignore includes:
cat .gitignore | grep ".env"
```

## Part 2: Deploy Backend to Render

### Step 1: Create Render Account & Service

1. Go to https://render.com
2. Sign up / Log in
3. Click "New +" → "Web Service"
4. Select "Connect a repository" → Choose your repository

### Step 2: Configure Service

**Build Settings:**
```
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Environment Variables:**
```
GEMINI_API_KEY          = your_gemini_api_key
EMAIL_USER              = your_email@gmail.com
EMAIL_PASS              = your_app_password
FRONTEND_URL            = https://your-frontend.vercel.app
ENVIRONMENT             = production
```

### Step 3: Deploy

1. Click "Create Web Service"
2. Wait for initial build (~5 minutes)
3. Note the service URL (e.g., https://sales-automator-backend.onrender.com)
4. Test health endpoint: `https://your-service.onrender.com/health`

### Step 4: Setup Auto-Deploy

1. In Render dashboard → Auto-deploy: Enable "Deploy on push"
2. Select branch: "main"
3. GitHub Actions workflows will handle deployment

## Part 3: Deploy Frontend to Vercel

### Step 1: Create Vercel Account

1. Go to https://vercel.com
2. Sign up / Log in
3. Click "New Project"
4. Select your repository

### Step 2: Configure Project

**Framework:** Vite
**Root Directory:** frontend
**Build Command:** `npm run build`
**Output Directory:** dist

### Step 3: Set Environment Variables

1. Project Settings → Environment Variables
2. Add:
   ```
   VITE_API_URL = https://your-render-backend.onrender.com
   ```

### Step 4: Deploy

1. Click "Deploy"
2. Wait for build completion (~2 minutes)
3. Note the deployment URL (e.g., https://sales-automator.vercel.app)
4. Test application in browser

## Part 4: Setup GitHub Actions

### Step 1: Generate Render API Key

1. In Render dashboard → Account Settings → API Keys
2. Create new API key, copy it
3. Save as GitHub secret: `RENDER_API_KEY`

### Step 2: Get Render Service ID

1. In Render dashboard → Services → Your backend service
2. URL contains service ID: `https://dashboard.render.com/d?srv=srv_xxxx`
3. Save as GitHub secret: `RENDER_SERVICE_ID`

### Step 3: Get Vercel Tokens

1. https://vercel.com/account/tokens
2. Create new token, copy it
3. Save as GitHub secret: `VERCEL_TOKEN`

4. Vercel Project Settings → Project ID
   Save as: `VERCEL_PROJECT_ID`

5. Vercel Team Settings → Team ID
   Save as: `VERCEL_ORG_ID`

### Step 4: Add GitHub Secrets

In your GitHub repository:

1. Settings → Secrets and variables → Actions
2. New repository secret for each:

```
RENDER_API_KEY          = [from Render]
RENDER_SERVICE_ID       = [from Render]
VERCEL_TOKEN            = [from Vercel]
VERCEL_ORG_ID           = [from Vercel]
VERCEL_PROJECT_ID       = [from Vercel]
VITE_API_URL            = https://your-render-backend.onrender.com
```

## Part 5: Test Deployment

### Test Backend

```bash
# Health check
curl https://your-backend.onrender.com/health

# Get version
curl https://your-backend.onrender.com/
```

### Test Frontend

1. Open https://your-frontend.vercel.app in browser
2. Upload a CSV file
3. Enter email address
4. Click "Generate AI Summary"
5. Check email for summary

### Test Full Pipeline

1. Make code change in `backend/app/main.py` or `frontend/src/App.jsx`
2. Commit and push to main: `git push origin main`
3. Watch GitHub Actions → Workflows
4. Verify auto-deployment to Render/Vercel

## Part 6: Production Optimization

### Performance

1. **Backend (Render):**
   - Upgrade plan for more concurrent requests
   - Enable auto-scaling if available
   - Monitor CPU/Memory in dashboard

2. **Frontend (Vercel):**
   - Enable "Regions" for global edge caching
   - Check analytics for performance metrics
   - Use "Analytics" for real user monitoring

### Monitoring

1. **Render:**
   - Logs: Services → Your service → Logs
   - Metrics: Monitor CPU, Memory, requests
   - Alerts: Set up for crashes/errors

2. **Vercel:**
   - Analytics dashboard shows real user data
   - Error logging via Sentry integration
   - Performance metrics for builds

### Troubleshooting Deployments

**Backend won't deploy:**
- Check build logs in Render dashboard
- Verify requirements.txt syntax
- Ensure PYTHONUNBUFFERED=1 is set

**Frontend won't deploy:**
- Check build logs in Vercel dashboard
- Verify npm install succeeds
- Check for TypeScript errors

**API connection fails:**
- Verify VITE_API_URL in Vercel environment
- Check CORS settings in backend
- Monitor browser dev console for errors

## Part 7: Domain Configuration (Optional)

### Add Custom Domain to Render
1. Render dashboard → Service → Settings → Custom domains
2. Add your domain (e.g., api.yourdomain.com)
3. Follow DNS configuration instructions
4. Update FRONTEND_URL env var if needed

### Add Custom Domain to Vercel
1. Vercel dashboard → Project → Settings → Domains
2. Add your domain (e.g., yourdomain.com)
3. Follow DNS configuration instructions
4. Update VITE_API_URL if using custom backend domain

## Maintenance Checklist

- [ ] Monitor error logs weekly
- [ ] Update dependencies monthly
- [ ] Review API usage and costs
- [ ] Backup important data
- [ ] Test disaster recovery
- [ ] Keep API keys rotated
- [ ] Review security advisories

## Rollback Procedure

### If deployment fails:

**Render:**
1. Dashboard → Service → Deploys
2. Select previous successful deploy
3. Click "Redeploy"

**Vercel:**
1. Dashboard → Project → Deployments
2. Find last working deployment
3. Click "Promote to Production"

## Support

- **Render Docs:** https://render.com/docs
- **Vercel Docs:** https://vercel.com/docs
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **React Docs:** https://react.dev
