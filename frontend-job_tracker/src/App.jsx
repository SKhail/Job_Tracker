import React from "react";
import "./App.css";
import JobList from "./components/JobList";

function App() {
  return (
    <>
      <div className="p-4">
        <h1 className="font-bold text-xl">Job Tracker </h1>
        <JobList />
      </div>
    </>
  );
}

export default App;
