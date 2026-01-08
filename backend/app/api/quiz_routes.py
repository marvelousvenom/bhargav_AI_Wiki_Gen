from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.services.quiz_service import process_quiz
from app.utils.validators import validate_wikipedia_url

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)

# =========================
# DB Dependency
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# Generate Quiz Endpoint
# =========================
@router.post("/generate")
def generate_quiz(
    url: str,
    db: Session = Depends(get_db)
):
    # 1️⃣ Validate URL
    if not validate_wikipedia_url(url):
        raise HTTPException(
            status_code=400,
            detail="Invalid Wikipedia URL"
        )

    # 2️⃣ Process Quiz
    try:
        quiz_data = process_quiz(url, db)
        return quiz_data

    except ValueError as e:
        # Logical / validation errors
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        # Unexpected errors
        raise HTTPException(
            status_code=500,
            detail="Failed to generate quiz. Please try again."
        )
