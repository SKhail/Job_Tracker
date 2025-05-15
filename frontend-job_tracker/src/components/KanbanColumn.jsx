import React from "react";

const KanbanColumn = ({ title, status, jobs, handleDragStart, handleDrop }) => {
  //Use state to store the hard corded jobs

  return (
    <div className=" w-1/4 h-[20rem] bg-gray-500  text-white" onDrop={(e) => handleDrop(e, status)} onDragOver={(e) => e.preventDefault()}>
      <h2>{title}</h2>
      {jobs
        .filter((job) => job.status === status)
        .map((job) => (
          <div key={job.id} className="m-2 p-2 bg-white text-black rounded shadow" draggable onDragStart={(e) => handleDragStart(e, job.id)}>
            <h3 className="font-bold text-center">{job.title}</h3>
            <p className="text-center">{job.company}</p>
          </div>
        ))}
    </div>
  );
};

export default KanbanColumn;
