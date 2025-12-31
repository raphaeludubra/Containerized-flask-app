# Containerized Flask Web App with PostgreSQL

A simple backend web application built with **Flask** and **PostgreSQL**, fully containerized using **Docker** and orchestrated with **Docker Compose**.  
The project demonstrates how to build, run, and persist a production-style web service in a reproducible environment.

---

## 🚀 Features
- REST API built with Flask
- PostgreSQL database for persistent storage
- SQLAlchemy ORM for database interaction
- Gunicorn production-grade web server
- Dockerized services for portability
- Docker Compose for multi-container orchestration
- Persistent data using Docker volumes

---

## 🧱 Architecture Overview

``
Client (Browser / curl)
|
v
Flask API (Gunicorn)
|
v
PostgreSQL Database


- The Flask app and database run in **separate containers**
- Containers communicate via an internal Docker network
- Database data persists across restarts using a Docker volume

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Server:** Gunicorn
- **Containerization:** Docker, Docker Compose

## 📌 What This Project Can Be Used For

This project serves as a **backend service template** for applications that require a web API, a database, and a reproducible deployment environment.

### Practical Use Cases
- **Backend for simple applications** such as task managers, study trackers, expense trackers, or note-taking apps
- **Internal tools** for collecting data, managing jobs, or tracking system state
- **Microservice foundation** within a larger distributed system
- **Learning and experimentation** with REST APIs, databases, and containerization
- **Deployment-ready base** for cloud platforms that support Docker containers

The current implementation exposes task-based endpoints, but the structure is intentionally generic and can be easily adapted to support different data models or business logic.

### Why This Matters
This project demonstrates:
- Client → API → Database request flow
- Containerized service architecture
- Persistent data storage using Docker volumes
- Environment-independent deployment using Docker Compose

---
## ⚙️ Getting Started
### Prerequisites
- Docker Desktop (macOS / Windows / Linux)
---
## ▶️ How to Run the Application

Follow the steps below to run the application locally using Docker.

### Prerequisites
- Docker Desktop installed and running

Verify installation:
```bash
docker --version
docker compose version

Step 1: Clone the Repository
git clone git@github.com:raphaeludubra/Containerized-flask-app.git
cd Containerized-flask-app

Step 2: Build and Start the Containers
docker compose up --build


This command will:

Build the Flask application image

Start the PostgreSQL database container

Start the Flask API using Gunicorn

Step 3: Access the Application

Once the containers are running, access the app at:

http://localhost:5000


Health check endpoint:

http://localhost:5000/health


Expected response:

{ "status": "ok" }

Step 4: Test the API (Optional)

Create a task:

curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"My first task"}'


Retrieve all tasks:

curl http://localhost:5000/tasks

Step 5: Stop the Application

To stop the containers, press Ctrl + C, then run:

docker compose down


Database data will persist across restarts due to Docker volumes.
---
👤 Author
Raphael Udubra
Computer Science student with interests in backend systems, containers, and distributed applications.
