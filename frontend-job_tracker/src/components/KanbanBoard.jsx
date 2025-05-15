import React, { useState } from "react";
import KanbanColumn from "./KanbanColumn";

const mockData = [
  {
    id: 1,
    title: "Fix Login Bug",
    company: "Acme",
    status: "To Do", // or "In-Progress", "Done"
  },
  {
    id: 2,
    title: "UI Problem",
    company: "Task",
    status: "In Progress", // or "In Progress", "Done"
  },
  {
    id: 3,
    title: "Fix Login Bug",
    company: "JJ",
    status: "Done", // or "In-Progress", "Done"
  },
];

const KanbanBoard = () => {
  const [jobs, setJobs] = useState([...mockData]);
  const [draggingJobId, setDraggingJobId] = useState(null);

  // function to drag over feature
  const handleDragStart = (e, jobId) => {
    setDraggingJobId(jobId);
  };

  const handleDrop = (e, newStatus) => {
    setJobs((prevJobs) => prevJobs.map((jobs) => (jobs.id === draggingJobId ? { ...jobs, status: newStatus } : jobs)));
    setDraggingJobId(null);
  };

  return (
    <>
      <div className="text-center flex flex-nowrap justify-center overflow-x-auto  gap-4 py-5">
        <KanbanColumn title="To Do" status="To Do" jobs={jobs} handleDragStart={handleDragStart} handleDrop={handleDrop} />
        <KanbanColumn title="In Progress" status="In Progress" jobs={jobs} handleDragStart={handleDragStart} handleDrop={handleDrop} />
        <KanbanColumn title="Done" status="Done" jobs={jobs} handleDragStart={handleDragStart} handleDrop={handleDrop} />
      </div>
    </>
  );
};

export default KanbanBoard;
