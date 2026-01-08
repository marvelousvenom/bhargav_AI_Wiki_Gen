from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.crud import get_all_quizzes

router = APIRouter(
    prefix="/history",
    tags=["History"]
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
# Get Quiz History
# =========================
@router.get("/")
def get_quiz_history(db: Session = Depends(get_db)):
    try:
        quizzes = get_all_quizzes(db)

        return {
            "count": len(quizzes),
            "data": quizzes
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to load quiz history"
        )
