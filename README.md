# Sales Insight Automator

AI-powered sales report generator that analyzes CSV files and sends personalized AI-generated summaries via email.

## 🚀 Features

- **CSV Upload**: Upload sales data in CSV format
- **AI Analysis**: Automatic analysis using Google Gemini API
- **Email Delivery**: Auto-send summaries to specified email addresses
- **Production Ready**: Full CI/CD pipeline with automated testing and deployment
- **Scalable Architecture**: FastAPI backend + React frontend

## 📋 Tech Stack

**Backend:**
- FastAPI (Python web framework)
- Pandas (Data analysis)
- Google Generativeai (AI summaries)
- SQLite/PostgreSQL ready

**Frontend:**
- React 19
- Vite (Fast build tool)
- TailwindCSS ready

**Deployment:**
- Render (Backend hosting)
- Vercel (Frontend hosting)
- Docker (Containerization)

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

### Backend Setup

1. **Create virtual environment:**
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create .env file:**
```bash
cp ../.env.example backend/.env
```

4. **Configure environment variables:**
```env
GEMINI_API_KEY=your_gemini_api_key_here
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_specific_password_here
FRONTEND_URL=http://localhost:3000
ENVIRONMENT=development
```

> **Note:** Get your Gemini API key from [Google AI Studio](https://aistudio.google.com)
> For Gmail: Use [App-specific passwords](https://support.google.com/accounts/answer/185833)

5. **Run backend:**
```bash
uvicorn app.main:app --reload
```

Backend runs at `http://localhost:8000`

### Frontend Setup

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Create .env file:**
```bash
cp .env.example .env
```

3. **Configure API endpoint:**
```env
VITE_API_URL=http://localhost:8000
```

4. **Run development server:**
```bash
npm run dev
```

Frontend runs at `http://localhost:5173`

## 📦 API Endpoints

### Health Check
```
GET /health
GET /
```

### Upload & Process CSV
```
POST /api/upload
Content-Type: multipart/form-data

Parameters:
- file: CSV file (required)
- email: recipient email (required)
```

**Response:**
```json
{
  "message": "AI summary generated",
  "email_sent": true,
  "analysis": {
    "total_revenue": 150000,
    "top_region": "North America",
    "top_product": "Premium Plan"
  },
  "summary_preview": "..."
}
```

## 🐳 Docker Setup

### Build Image
```bash
docker build -f backend/DockerFile -t sales-automator-backend .
```

### Run Container
```bash
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your_key \
  -e EMAIL_USER=your_email \
  -e EMAIL_PASS=your_password \
  -e FRONTEND_URL=your_frontend_url \
  sales-automator-backend
```

### Docker Compose
```bash
docker-compose up -d
```

## 🚀 Production Deployment

### Option 1: Deploy to Render (Backend)

1. **Create Render account** at [render.com](https://render.com)

2. **Create new Web Service:**
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
   - Add environment variables:
     - `GEMINI_API_KEY`: Your Gemini API key
     - `EMAIL_USER`: Gmail address
     - `EMAIL_PASS`: App-specific password
     - `FRONTEND_URL`: Your Vercel frontend URL
     - `ENVIRONMENT`: `production`

3. **Deploy:**
   - Push to main branch - auto-deploys via GitHub Actions
   - Or manually deploy from Render dashboard

4. **Note backend URL** for frontend configuration

### Option 2: Deploy to Vercel (Frontend)

1. **Create Vercel account** at [vercel.com](https://vercel.com)

2. **Connect GitHub repository:**
   - Select `frontend` as root directory
   - Set Node version to 18

3. **Configure environment:**
   - `VITE_API_URL`: Your Render backend URL

4. **Deploy:**
   - Auto-deploys on push to main
   - Or manually from Vercel dashboard

## 🔄 GitHub Actions CI/CD Pipeline

The project includes automated:

### Testing Workflows
- **test-backend.yml**: Python linting, imports check, code quality
- **test-frontend.yml**: ESLint, build verification

### Deployment Workflows
- **deploy-backend.yml**: Auto-deploys backend to Render on push
- **deploy-frontend.yml**: Auto-deploys frontend to Vercel on push

### GitHub Secrets Required

**For Render (Backend):**
- `RENDER_API_KEY`: From Render dashboard
- `RENDER_SERVICE_ID`: Your backend service ID

**For Vercel (Frontend):**
- `VERCEL_TOKEN`: From Vercel dashboard
- `VERCEL_ORG_ID`: Your organization ID
- `VERCEL_PROJECT_ID`: Your project ID
- `VITE_API_URL`: Your Render backend URL

### Setup GitHub Secrets

1. Go to GitHub repository → Settings → Secrets and variables → Actions
2. Add each secret from above
3. Workflows will run automatically on push to main

## 📋 Sample CSV Format

```csv
Date,Region,Product_Category,Revenue,Units_Sold
2024-01-15,North America,Premium Plan,5000,10
2024-01-15,Europe,Standard Plan,3000,15
2024-01-16,Asia,Premium Plan,4500,9
```

**Required columns:**
- `Revenue` (numbers)
- `Region` (text)
- `Product_Category` (text)

## 🧪 Testing

### Backend Tests
```bash
cd backend
pip install pytest pytest-cov
pytest --cov=app
```

### Frontend Tests
```bash
cd frontend
npm run lint
npm run build
```

## 🔒 Security Checklist

- [x] Environment variables not committed (.gitignore)
- [x] CORS configured for specific domains
- [x] Input validation on API endpoints
- [x] Error handling with logging
- [x] File size limits (10MB max)
- [x] Email validation
- [x] API health check endpoint

## 📊 Project Structure

```
sales-insight-automator/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── routes/
│   │   │   └── upload.py
│   │   └── services/
│   │       ├── csv_service.py
│   │       ├── llm_service.py
│   │       └── email_service.py
│   ├── requirements.txt
│   └── DockerFile
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── .github/
│   └── workflows/
│       ├── deploy-backend.yml
│       ├── deploy-frontend.yml
│       ├── test-backend.yml
│       └── test-frontend.yml
├── vercel.json
├── render.yaml
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🐛 Troubleshooting

### Backend Issues

**404 on API endpoint:**
- Check backend is running: `http://localhost:8000/`
- Check FRONTEND_URL env var includes correct origin

**Email not sending:**
- Verify Gmail app-specific password
- Check SMTP credentials
- Enable "Less secure app access" if not using app password

**Gemini API error:**
- Verify GEMINI_API_KEY is correct
- Check API quota at Google AI Studio

### Frontend Issues

**API connection failed:**
- Check VITE_API_URL environment variable
- Verify backend is accessible
- Check browser console for CORS errors

**Build fails:**
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node version: `node --version` (should be 18+)

## 📝 Environment Variables Reference

### Backend (.env)
```
GEMINI_API_KEY=       # Google Gemini API key
EMAIL_USER=           # Gmail address
EMAIL_PASS=           # Gmail app-specific password
FRONTEND_URL=         # Frontend base URL (for CORS)
ENVIRONMENT=          # development/production
SMTP_SERVER=          # smtp.gmail.com (default)
SMTP_PORT=            # 587 (default)
```

### Frontend (.env)
```
VITE_API_URL=         # Backend API URL
```

## 📞 Support & Contact

For issues, questions, or improvements:
1. Check troubleshooting section above
2. Review GitHub Issues
3. Create a new issue with detailed description

## 📄 License

MIT License - feel free to use for any purpose

## 🎯 Future Enhancements

- [ ] Database integration for file history
- [ ] User authentication & accounts
- [ ] Multiple file format support (Excel, JSON)
- [ ] Advanced analytics dashboard
- [ ] Webhook integration
- [ ] API rate limiting
- [ ] Batch processing
- [ ] Custom report templates
