from sqlalchemy.orm import Session
from app.database.models import WikiQuiz

def get_all_quizzes(db: Session):
    quizzes = (
        db.query(WikiQuiz)
        .order_by(WikiQuiz.created_at.desc())
        .all()
    )

    return [
        {
            "id": q.id,
            "url": q.url,
            "title": q.title,
            "created_at": q.created_at,
            "quiz": q.quiz
        }
        for q in quizzes
    ]
