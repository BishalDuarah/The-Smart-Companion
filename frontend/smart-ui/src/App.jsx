import { useState } from "react";
import ProfileForm from "./screens/ProfileForm";
import TaskInput from "./screens/TaskInput";
import StepView from "./screens/StepView";
import FontToggle from "./components/FontToggle";

export default function App() {
  const [stage, setStage] = useState("profile");
  const [taskId, setTaskId] = useState(null);
  const [font, setFont] = useState("font-lexend");

  return (
    <div className={`${font} min-h-screen`}>
      <FontToggle setFont={setFont} />

      {stage === "profile" && (
        <ProfileForm onDone={() => setStage("task")} />
      )}

      {stage === "task" && (
        <TaskInput
          onTaskCreated={(id) => {
            setTaskId(id);
            setStage("steps");
          }}
        />
      )}

      {stage === "steps" && (
        <StepView taskId={taskId} />
      )}
    </div>
  );
}
