import { useEffect, useState } from "react";
import TakeQuiz from "../components/TakeQuiz";
import HistoryTable from "../components/HistoryTable";

const API_BASE = "https://bhargav-ai-wiki-gen.onrender.com";

function Home() {
  const [activeTab, setActiveTab] = useState("generate");
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [history, setHistory] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  /* =========================
     Generate Quiz
  ========================== */
  const generateQuiz = async () => {
    if (!url.trim()) {
      setError("Please enter a Wikipedia URL");
      return;
    }

    setError("");
    setQuiz(null);
    setLoading(true);

    try {
      const res = await fetch(
        `${API_BASE}/quiz/generate?url=${encodeURIComponent(url)}`,
        { method: "POST" }
      );

      if (!res.ok) throw new Error();

      const data = await res.json();
      setQuiz(data);
    } catch {
      setError("Failed to generate quiz");
    } finally {
      setLoading(false);
    }
  };

  /* =========================
     Load History
  ========================== */
  const loadHistory = async () => {
    try {
      const res = await fetch(`${API_BASE}/history`);
      const data = await res.json();
      setHistory(data);
    } catch {
      setError("Failed to load quiz history");
    }
  };

  useEffect(() => {
    if (activeTab === "history") {
      loadHistory();
    }
  }, [activeTab]);

  return (
    <div className="container">
      {/* ===== Tabs ===== */}
      <div className="tabs">
        <button
          className={activeTab === "generate" ? "active" : ""}
          onClick={() => {
            setActiveTab("generate");
            setQuiz(null);
          }}
        >
          Generate Quiz
        </button>

        <button
          className={activeTab === "history" ? "active" : ""}
          onClick={() => {
            setActiveTab("history");
            setQuiz(null);
          }}
        >
          Quiz History
        </button>
      </div>

      {/* ===== TAB 1: Generate Quiz ===== */}
      {activeTab === "generate" && (
        <>
          <div className="input-group">
            <input
              type="text"
              placeholder="Paste Wikipedia URL"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
            <button onClick={generateQuiz} disabled={loading}>
              {loading ? "Generating..." : "Generate"}
            </button>
          </div>

          {quiz && <TakeQuiz quiz={quiz} />}
        </>
      )}

      {/* ===== TAB 2: Quiz History ===== */}
      {activeTab === "history" && (
        <HistoryTable history={history} />
      )}

      {/* ===== Error ===== */}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default Home;
