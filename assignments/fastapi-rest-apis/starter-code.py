from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TaskIn(BaseModel):
    title: str
    description: str
    completed: bool = False

class Task(TaskIn):
    id: int

# In-memory task list for the assignment.
# Students can replace this with a database later if desired.
tasks: List[Task] = [
    Task(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False),
    Task(id=2, title="Finish homework", description="Complete the FastAPI assignment", completed=False),
]

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_in: TaskIn):
    new_id = max([task.id for task in tasks]) + 1 if tasks else 1
    new_task = Task(id=new_id, **task_in.dict())
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_in: TaskIn):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(id=task_id, **task_in.dict())
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")
