from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.services.quiz_service import process_quiz
from app.utils.validators import validate_wikipedia_url

router = APIRouter(prefix="/quiz", tags=["Quiz"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/generate")
def generate_quiz(url: str, db: Session = Depends(get_db)):
    if not validate_wikipedia_url(url):
        raise HTTPException(status_code=400, detail="Invalid Wikipedia URL")

    return process_quiz(url, db)
