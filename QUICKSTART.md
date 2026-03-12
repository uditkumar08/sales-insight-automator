# Quick Start Guide

Get Sales Insight Automator running in minutes!

## 🚀 Development (30 seconds)

### Windows
```bash
setup.bat
```

### macOS/Linux
```bash
bash setup.sh
```

This will:
- ✓ Check prerequisites
- ✓ Set up Python virtual environment
- ✓ Install backend & frontend dependencies
- ✓ Create configuration files
- ✓ Guide you through next steps

## 📝 Configure API Keys

Edit `backend/.env`:

1. **Get Gemini API Key:**
   - Visit: https://aistudio.google.com
   - Click "Get API Key"
   - Copy key to .env

2. **Setup Gmail:**
   - Enable 2-Step Verification on account
   - Create App Password: https://myaccount.google.com/apppasswords
   - Copy to .env as EMAIL_PASS

## ▶️ Start Development Servers

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
uvicorn app.main:app --reload
```
Backend at: http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend at: http://localhost:5173

## 🧪 Test the Application

1. Open http://localhost:5173
2. Create a test CSV with headers: `Date,Region,Product_Category,Revenue,Units_Sold`
3. Add some sample data
4. Upload file + enter email
5. Click "Generate AI Summary"
6. Check email for AI-generated summary

## 📦 Docker Development

```bash
# Build and run all services
docker-compose up

# Or with frontend development
docker-compose --profile dev up
```

## 🚀 Production Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions:

1. Push to GitHub
2. Deploy backend to Render (1 click)
3. Deploy frontend to Vercel (1 click)
4. CI/CD automatically handles updates

## 📚 Documentation

- **API Reference:** http://localhost:8000/docs (Swagger UI)
- **Full README:** [README.md](README.md)
- **Deployment:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 🆘 Common Issues

**API connection fails?**
- Check backend is running: http://localhost:8000/health
- Check VITE_API_URL in frontend/.env

**Email not sending?**
- Verify Gmail app password
- Check EMAIL_USER and EMAIL_PASS in backend/.env

**Build errors?**
- Clear and reinstall: `rm -rf node_modules && npm install`
- Check Node version: `node --version` (need 18+)

## 🎯 Next Steps

1. ✅ Customize CSV columns for your data
2. ✅ Add database support (currently file-based)
3. ✅ Deploy to production
4. ✅ Add authentication
5. ✅ Create dashboards

---

**Questions?** Check [README.md](README.md) or create a GitHub issue!
