import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import KanbanColumn from "../src/components/KanbanColumn";

const mockJobs = [
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
];

test("renders jobs with status To Do", () => {
  render(<KanbanColumn title="To Do" status="To Do" jobs={mockJobs} />);

  // Check that the title renders
  expect(screen.getByText("To Do")).toBeInTheDocument();

  // Check that the job title renders
  expect(screen.getByText("Fix Login Bug")).toBeInTheDocument();

  // Make sure "UI Problem" is NOT shown
  expect(screen.queryByText("UI Problem")).not.toBeInTheDocument();
});
