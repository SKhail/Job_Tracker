import React from "react";
import "./App.css";
import KanbanBoard from "./components/KanbanBoard";

function App() {
  return (
    <>
      <div className="p-4">
        <h1 className="font-bold text-xl">Job Tracker </h1>
        <KanbanBoard />
      </div>
    </>
  );
}

export default App;
