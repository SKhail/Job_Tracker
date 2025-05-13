import React from "react";

const KanbanColumn = ({ title, status, jobs }) => {
  return (
    <>
      <div className="flex justify-center mb-4">
        <div className="w-1/4 bg-gray-700 h-[20rem] text-center text-white">
          {title}
          {jobs
            .filter((job) => job.status === status)
            .map((job) => (
              <div key={job.id} className="m-2 p-2 bg-white text-black rounded shadow">
                <h3 className="font-bold text-center">{job.title}</h3>
                <p className="text-center">{job.company}</p>
              </div>
            ))}
        </div>
      </div>
    </>
  );
};

export default KanbanColumn;
