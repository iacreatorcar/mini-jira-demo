# Mini Jira Demo

A simple demo application for task management, inspired by Jira.  
Developed by Carmine Dalise using Python (Flask), HTML, and CSS.

---

## Project Overview

This demo project simulates a basic Kanban board for managing tasks, similar to the core features of Jira.  
It is intended to showcase technical skills in web application development and containerization using Docker.

Key components:
- **Frontend:** HTML and CSS for structure and styling
- **Backend:** Python with Flask for routing and business logic
- **Containerization:** Full application packaged and runnable with Docker

---

## Main Features

- Add tasks with title and description
- Display tasks by status: "To Do", "In Progress", "Done"
- Move tasks between statuses

---

## Quick Start (Docker)

1. Open terminal in the project directory
2. Build the Docker image:
    ```
    docker build -t mini-jira-demo .
    ```
3. Run the container (exposes the app on port 5001):
    ```
    docker run -d -p 5001:5000 mini-jira-demo
    ```
4. Access the application in your browser at:
    ```
    http://localhost:5001
    ```

---

## Technologies Used

- Python 3 (Flask)
- HTML/CSS
- Docker

---

## Purpose

This public demo is designed for recruitment and technical evaluation purposes.  
It demonstrates the ability to build and containerize a simple, functional web application from scratch.

---

**Developed by Carmine Dalise**
