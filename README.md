# Mini Jira Demo

A simple demo web application for task management, inspired by Jira.  
Developed by Carmine Dalise using Python (Flask), HTML, CSS, and Docker.

---

## Project Overview

This application simulates a basic Kanban board to track the progress of tasks in a software or facilities management environment.  
It demonstrates key skills in web development, code organization, and containerization with Docker.

---

## Features

- Add tasks with title, description (with ID), assigned team member, and due date.
- Visualize tasks by status: **To Do**, **In Progress**, **Done**.
- View the latest updates for each task.
- Move tasks between statuses with one click.
- Responsive and clean web interface.

---

## Live Demo (Local)

After running this application with Docker (see below), access from your browser at:  
**[http://localhost:5001/](http://localhost:5001/)**

---

## How to Run with Docker

1. Make sure you have [Docker](https://www.docker.com/) installed and running on your system.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate into the project folder.
4. Build the Docker image:
    ```
    docker build -t mini-jira-demo .
    ```
5. Run the container (mapping port 5001 on your computer to port 5000 in the container):
    ```
    docker run -d -p 5001:5000 mini-jira-demo
    ```
6. Open your browser and navigate to:
    ```
    http://localhost:5001/
    ```

---

## Example Tasks Preloaded

The board is preloaded with realistic example tasks, each with a title, ID, assignee, due date, status, and updates:
- **To Do:**  
    - Port Provisioning  
    - Gala Dinner Prep
- **In Progress:**  
    - AC Repair Suite 704  
    - Sound Check: Theater
- **Done:**  
    - Bridge Safety Check  
    - Pool Water Quality Test

---

## Technologies Used

- Python 3 (Flask web framework)
- HTML and CSS
- Docker

---

## Purpose

This project is intended as a public demonstration for technical and recruitment evaluation, highlighting Docker proficiency, basic fullstack workflow, and simple task management logic.

---

**Developed by Carmine Dalise**
