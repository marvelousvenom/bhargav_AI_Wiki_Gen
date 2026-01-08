from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.database import engine
from app.database.models import Base
from app.api.quiz_routes import router as quiz_router
from app.api.history_routes import router as history_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

#FIXED CORS (supports Vercel + local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://bhargav-ai-wiki-gen.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz_router)
app.include_router(history_router)

@app.get("/")
def root():
    return {"status": "AI Wiki Quiz Generator running"}
