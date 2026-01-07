from sqlalchemy.orm import Session
from app.database.models import WikiQuiz

def get_quiz_by_url(db: Session, url: str):
    return db.query(WikiQuiz).filter(WikiQuiz.url == url).first()

def create_quiz(db: Session, data: dict):
    quiz = WikiQuiz(**data)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def get_all_quizzes(db: Session):
    return db.query(WikiQuiz).order_by(WikiQuiz.created_at.desc()).all()
