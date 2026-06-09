# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework. Students will create endpoints to handle common HTTP methods, validate request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Create the API structure

#### Description
Build a FastAPI application with at least three endpoints for a simple task management API.

#### Requirements
Completed project should:

- Create a FastAPI app instance in `starter-code.py`.
- Provide endpoints for:
  - `GET /tasks` to return a list of all tasks.
  - `GET /tasks/{task_id}` to return a specific task by id.
  - `POST /tasks` to add a new task.
- Use JSON request and response bodies.

### 🛠️ Add data validation and response models

#### Description
Use FastAPI models to validate request payloads and define the structure of task responses.

#### Requirements
Completed project should:

- Define a Pydantic model for incoming task data with fields `title`, `description`, and `completed`.
- Define a response model for tasks that includes `id`, `title`, `description`, and `completed`.
- Validate the `POST /tasks` request body and return a `201 Created` response with the created task.

### 🛠️ Implement update and delete behavior

#### Description
Extend the API to allow students to update and delete tasks.

#### Requirements
Completed project should:

- Provide a `PUT /tasks/{task_id}` endpoint to update an existing task.
- Provide a `DELETE /tasks/{task_id}` endpoint to remove a task.
- Return appropriate status codes for successful updates and deletions.
- Return a meaningful error response if a task is not found.
