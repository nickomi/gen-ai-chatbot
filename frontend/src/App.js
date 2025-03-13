import { useState } from "react";

export default function ChatbotUI() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch(`http://localhost:8000/chat?query=${message}`);
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div>
      <h1>Generative AI Chatbot</h1>
      <input value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
      <p>Response: {response}</p>
    </div>
  );
}