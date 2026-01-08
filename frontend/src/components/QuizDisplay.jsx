function QuizDisplay({ quiz }) {
  if (!quiz) return null;

  return (
    <div className="quiz-section">
      <h2 className="quiz-title">{quiz.title}</h2>

      {quiz.quiz.map((q, index) => (
        <div className="question-card" key={index}>
          <p className="question">
            {index + 1}. {q.question}
          </p>

          <ul className="options">
            {q.options.map((opt, i) => (
              <li key={i}>{opt}</li>
            ))}
          </ul>

          <p className="answer">Answer: {q.answer}</p>
        </div>
      ))}
    </div>
  );
}

export default QuizDisplay;
