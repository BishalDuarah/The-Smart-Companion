import { useState } from "react";

export default function TaskInput({ onTaskCreated }) {
  const [task, setTask] = useState("");

  const handleSubmit = async () => {
    if (!task.trim()) return;

    const res = await fetch("/task/user1",
 {

      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task }),
    });

    const data = await res.json();

    // Pass task_id to App.jsx
    onTaskCreated(data.task_id);
  };

  const startVoice = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.onresult = (event) => {
      setTask(event.results[0][0].transcript);
    };
    recognition.start();
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-8 p-10 text-xl">
      <h1 className="text-3xl font-bold">What would you like to do?</h1>

      <textarea
        className="border p-4 w-96 rounded-xl"
        rows="3"
        placeholder="Type your task here..."
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />

      <div className="flex gap-6">
        <button
          onClick={startVoice}
          className="bg-gray-200 px-6 py-3 rounded-xl"
        >
          🎤 Speak
        </button>

        <button
          onClick={handleSubmit}
          className="bg-black text-white px-8 py-3 rounded-xl"
        >
          Break into Steps
        </button>
      </div>
    </div>
  );
}
