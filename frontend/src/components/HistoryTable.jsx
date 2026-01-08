import { useState } from "react";
import QuizDisplay from "./QuizDisplay";

function HistoryTable({ history }) {
  const [selectedQuiz, setSelectedQuiz] = useState(null);

  return (
    <div>
      <h2 className="quiz-title">Quiz History</h2>

      {history.length === 0 && <p>No quiz history found.</p>}

      <table className="history-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Title</th>
            <th>Created</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {history.map((item, index) => (
            <tr key={item.id}>
              <td>{index + 1}</td>
              <td>{item.title}</td>
              <td>{new Date(item.created_at).toLocaleString()}</td>
              <td>
                <button
                  className="details-btn"
                  onClick={() => setSelectedQuiz(item)}
                >
                  Details
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Modal */}
      {selectedQuiz && (
        <div className="modal-backdrop">
          <div className="modal">
            <button
              className="close-btn"
              onClick={() => setSelectedQuiz(null)}
            >
              ✕
            </button>

            <QuizDisplay quiz={selectedQuiz} />
          </div>
        </div>
      )}
    </div>
  );
}

export default HistoryTable;
