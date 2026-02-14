export default function FontToggle({ setFont }) {
  return (
    <div className="absolute top-5 right-5 flex gap-4">
      <button
        onClick={() => setFont("font-lexend")}
        className="px-4 py-2 border rounded"
      >
        Lexend
      </button>
      <button
        onClick={() => setFont("font-dyslexic")}
        className="px-4 py-2 border rounded"
      >
        OpenDyslexic
      </button>
    </div>
  );
}
