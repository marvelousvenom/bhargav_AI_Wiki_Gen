from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from datetime import datetime
from app.database.database import Base

class WikiQuiz(Base):
    __tablename__ = "wiki_quizzes"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String(500), nullable=False)
    title = Column(String(255), nullable=False)

    summary = Column(Text)
    quiz = Column(JSON, nullable=False)
    related_topics = Column(JSON)
    raw_html = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
