import React from "react";
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

// console.log(mockData);

const KanbanBoard = () => {
  console.log(mockData);
  return (
    <>
      <KanbanColumn title="To Do" status="To Do" jobs={mockData} />
      <KanbanColumn title="In Progress" status="In Progress" jobs={mockData} />
      <KanbanColumn title="Done" status="Done" jobs={mockData} />
    </>
  );
};

export default KanbanBoard;
