import { useEffect, useState } from "react";

export default function StepView({ taskId }) {
  const [steps, setSteps] = useState([]);
  const [current, setCurrent] = useState(0);
  const [streak, setStreak] = useState(0);

  const fetchSteps = async () => {
    const res = await fetch(`/steps/${taskId}`);
    const data = await res.json();
    setSteps(data.steps);
  };

  useEffect(() => {
    fetchSteps();
  }, []);

  const markDone = async () => {
    await fetch("/step/complete", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        task_id: taskId,
        step_number: steps[current].step_number,
      }),
    });

    setStreak(streak + 1);

    // Refresh steps from backend
    const res = await fetch(`/steps/${taskId}`);
    const data = await res.json();
    setSteps(data.steps);

    if (current < data.steps.length - 1) {
      setCurrent(current + 1);
    }
  };

  const speak = () => {
    const msg = new SpeechSynthesisUtterance(
      steps[current].step_text
    );
    speechSynthesis.speak(msg);
  };

  // ✅ Completion screen
  const allDone = steps.length > 0 && steps.every(s => s.completed);

  if (allDone) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center gap-8 text-3xl">
        <div>🎉 Task Completed!</div>
        <button
          onClick={() => window.location.reload()}
          className="bg-black text-white px-8 py-4 rounded-xl"
        >
          Start New Task
        </button>
      </div>
    );
  }

  if (steps.length === 0) {
    return <h2 className="p-10 text-2xl">Loading steps...</h2>;
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-8 p-10 text-2xl text-center">

      <div className="text-sm text-gray-500">
        Task ID: {taskId}
      </div>

      <div>
        Step {current + 1} of {steps.length}
      </div>

      {/* Progress bar */}
      <div className="w-96 h-3 bg-gray-200 rounded">
        <div
          className="h-3 bg-black rounded"
          style={{ width: `${((current + 1) / steps.length) * 100}%` }}
        />
      </div>

      {/* Step card */}
      <div className="border p-10 rounded-2xl w-[500px] shadow-lg">
        {steps[current].step_text}
      </div>

      <div className="text-lg text-gray-500">
        ⏱ ~2 minutes
      </div>

      <div>🔥 Streak: {streak}</div>

      <div className="flex gap-8">
        <button
          onClick={speak}
          className="bg-gray-200 px-6 py-3 rounded-xl"
        >
          🔊 Hear Step
        </button>

        <button
          onClick={markDone}
          className="bg-black text-white px-8 py-3 rounded-xl"
        >
          Done
        </button>
      </div>
    </div>
  );
}
