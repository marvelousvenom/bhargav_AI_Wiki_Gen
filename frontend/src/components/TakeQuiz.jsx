import { useState } from "react";

function TakeQuiz({ quiz }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);

  const handleSelect = (qIndex, option) => {
    setAnswers({ ...answers, [qIndex]: option });
  };

  const submitQuiz = () => {
    let correct = 0;

    quiz.quiz.forEach((q, index) => {
      if (answers[index] === q.answer) correct++;
    });

    setScore(correct);
    setSubmitted(true);
  };

  return (
    <>
      <h2 className="quiz-title">{quiz.title}</h2>

      {quiz.quiz.map((q, index) => (
        <div className="question-card" key={index}>
          <p className="question">
            {index + 1}. {q.question}
          </p>

          <ul className="options">
            {q.options.map((opt, i) => (
              <li key={i}>
                <label>
                  <input
                    type="radio"
                    name={`q-${index}`}
                    disabled={submitted}
                    onChange={() => handleSelect(index, opt)}
                  />
                  {opt}
                </label>
              </li>
            ))}
          </ul>

          {submitted && (
            <p className="answer">
              Correct Answer: <b>{q.answer}</b>
            </p>
          )}
        </div>
      ))}

      {!submitted && (
        <button className="submit-btn" onClick={submitQuiz}>
          Submit Quiz
        </button>
      )}

      {submitted && (
        <h3 className="score">
          Your Score: {score} / {quiz.quiz.length}
        </h3>
      )}
    </>
  );
}

export default TakeQuiz;
