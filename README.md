#  AI Wiki Quiz Generator

An AI-powered web application that generates interactive quizzes from Wikipedia articles using Large Language Models.

---

##  Live Demo

 Frontend: https://your-frontend.vercel.app  
 Backend API: https://your-backend.onrender.com/docs  

---

##  Tech Stack

### Frontend
- React (JavaScript)
- HTML, CSS
- Fetch API

### Backend
- FastAPI
- Python
- SQLAlchemy
- MySQL
- Groq LLM API

### Deployment
- Frontend: Vercel / Netlify
- Backend: Render
- Database: MySQL (Railway / PlanetScale / Local)

---

##  Features

-  Accepts any valid Wikipedia URL
-  AI-generated quiz questions
-  Multiple-choice format
-  Take Quiz mode with scoring
-  Caching to prevent duplicate scraping
-  Quiz history API
-  Fast and responsive UI

---

##  How It Works

1. User enters a Wikipedia article URL
2. Backend scrapes and summarizes content
3. LLM generates structured quiz questions
4. Frontend renders quiz
5. User submits answers and gets score

---

##  How to Run Locally

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
