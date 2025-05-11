import React from "react";

const KanbanBoard = () => {
  const mockData = [
    {
      id: 1,
      title: "Fix Login Bug",
      company: "Acme",
      status: "To Do", // or "In Progress", "Done"
    },
    {
      id: 2,
      title: "UI Problem",
      company: "Task",
      status: "In-Progress", // or "In Progress", "Done"
    },
    {
      id: 3,
      title: "Fix Login Bug",
      company: "JJ",
      status: "Done", // or "In Progress", "Done"
    },
  ];

  return (
    <>
      <div className="flex mb-4">
        <div className="w-1/3 bg-gray-700 h-[32rem] text-center text-white">
          To Do
          {mockData
            .filter((data) => data.status === "To Do")
            .map((mockData) => (
              <div key={mockData.id} className="m-2 p-2 bg-white text-black rounded shadow">
                <h3 className="font-bold text-center">{mockData.title}</h3>
                <p className="text-center">{mockData.company}</p>
              </div>
            ))}
        </div>
        <div className="w-1/3 bg-gray-500 h-[32rem] text-center text-white">
          In-Progress
          {mockData
            .filter((data) => data.status === "In-Progress")
            .map((mockData) => (
              <div key={mockData.id} className="m-2 p-2 bg-white text-black rounded shadow">
                <h3 className="font-bold text-center">{mockData.title}</h3>
                <p className="text-center">{mockData.company}</p>
              </div>
            ))}
        </div>
        <div className="w-1/3 bg-gray-400 h-[32rem] text-center text-white">
          Done
          {mockData
            .filter((data) => data.status === "Done")
            .map((mockData) => (
              <div key={mockData.id} className="m-2 p-2 bg-white text-black rounded shadow">
                <h3 className="font-bold text-center">{mockData.title}</h3>
                <p className="text-center">{mockData.company}</p>
              </div>
            ))}
        </div>
      </div>
    </>
  );
};

export default KanbanBoard;
