import { useState } from "react";

export default function ProfileForm({ onDone }) {
  const [form, setForm] = useState({
    reading_difficulty: false,
    attention_span: "low",
    time_blindness: false,
    prefers_extra_steps_for: ["kitchen"],
    font_preference: "lexend",
    needs_voice: true,
  });

  const handleSubmit = async () => {
    try {
      const res = await fetch("/profile/user1", {

        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });

      const data = await res.json();
      console.log("Profile saved:", data);

      onDone();
    } catch (error) {
      console.error("Error saving profile:", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-10 p-10 text-xl font-lexend">
      <h1 className="text-3xl font-bold">Tell us how to support you</h1>

      <label className="flex gap-4 items-center">
        <input
          type="checkbox"
          onChange={(e) =>
            setForm({ ...form, reading_difficulty: e.target.checked })
          }
        />
        Dense text is hard for me to read
      </label>

      <label className="flex gap-4 items-center">
        <input
          type="checkbox"
          onChange={(e) =>
            setForm({ ...form, time_blindness: e.target.checked })
          }
        />
        I lose track of time easily
      </label>

      <label className="flex gap-4 items-center">
        <input
          type="checkbox"
          onChange={(e) =>
            setForm({ ...form, needs_voice: e.target.checked })
          }
        />
        I prefer voice guidance
      </label>

      <button
        onClick={handleSubmit}
        className="bg-black text-white px-10 py-4 rounded-xl text-lg"
      >
        Save Profile
      </button>
    </div>
  );
}
