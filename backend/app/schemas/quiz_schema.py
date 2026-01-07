from pydantic import BaseModel
from typing import List, Optional

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str
    explanation: str

class QuizResponse(BaseModel):
    id: int
    url: str
    title: str
    summary: str
    quiz: List[QuizQuestion]
    related_topics: List[str]

    class Config:
        orm_mode = True
