import axios from "axios";
import React, { useState } from "react";
import l1 from "../images/l1.png";
import l2 from "../images/l2.jpeg";
import sendIcon from "../images/send-icon.png";

const QuestionPage = () => {
  // All States
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [isShow, setIsShow] = useState(false);

  // handler method for input field
  const handleQuestionChange = (e) => {
    setQuestion(e.target.value);
    setError(false);
  };

  // handler method to send question and receive answer
  const handleAskQuestion = async (e) => {
    e.preventDefault();
    setIsShow(true);
    try {
      setLoading(true);
      const response = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/question/1`,
        { question }
      );
      setAnswer(response.data);
      setLoading(false);
      setError(false);
    } catch (error) {
      setLoading(false);
      setError(true);
    }
  };

  return (
    <div className="wrapper">
      {/* Question-Answer part */}
      {isShow && question && (
        <div className="question">
          <img src={l2} alt="" />
          <p>{question}</p>
        </div>
      )}
      {loading ? (
        <h4>Loading.....</h4>
      ) : question && answer ? (
        <div className="answer">
          <img src={l1} alt="" />
          <p>{answer}</p>
        </div>
      ) : (
        error && <h4>Something went wrong.</h4>
      )}
      {/* Input field part */}
      <div className="input-wrapper">
        <form onSubmit={handleAskQuestion}>
          <input
            type="text"
            value={question}
            placeholder="Type your question here..."
            onChange={handleQuestionChange}
          />
          <button
            type="submit"
            style={{ background: "none", border: "none", padding: 0 }}
          >
            <img src={sendIcon} alt="Send" />
          </button>
        </form>
      </div>
    </div>
  );
};

export default QuestionPage;
