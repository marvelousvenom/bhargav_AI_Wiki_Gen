import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [error, setError] = useState("");

  const generateQuiz = async () => {
    setError("");
    setQuiz(null);

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/quiz/generate?url=${encodeURIComponent(url)}`,
        { method: "POST" }
      );

      if (!res.ok) throw new Error("Failed");

      const data = await res.json();
      setQuiz(data);
    } catch (err) {
      setError("Failed to generate quiz");
    }
  };

  return (
    <div className="container">
      <h1>AI Wiki Quiz Generator</h1>

      <div className="input-group">
        <input
          type="text"
          placeholder="Paste Wikipedia URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={generateQuiz}>Generate Quiz</button>
      </div>

      {error && <p className="error">{error}</p>}

      {quiz && (
        <>
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
        </>
      )}
    </div>
  );
}

export default App;
