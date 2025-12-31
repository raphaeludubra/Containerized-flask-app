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
### Clone the Repository
```bash
git clone git@github.com:raphaeludubra/Containerized-flask-app.git
cd Containerized-flask-app

Build and Run the App
docker compose up --build


The app will start at:

http://localhost:5000

🔍 API Endpoints
Health Check
GET /health


Response:

{ "status": "ok" }

Create a Task
POST /tasks
Content-Type: application/json


Request body:

{ "title": "My first task" }

List Tasks
GET /tasks


Response:

[
  { "id": 1, "title": "My first task" }
]

💾 Data Persistence

The PostgreSQL container uses a Docker volume, so data remains intact even after stopping and restarting containers.

Test persistence:

docker compose down
docker compose up


Previously created tasks will still be available.

🧪 Testing

Use curl to test endpoints:

curl http://localhost:5000/health
curl http://localhost:5000/tasks

🧹 Stopping the App
docker compose down

📌 Why This Project?

This project demonstrates:

Containerized backend development

Service-to-service communication

Persistent databases in Docker

Production-style application structure

Reproducible development environments

📈 Possible Improvements

Add full CRUD operations

Add Flask-Migrate (Alembic) for database migrations

Add authentication and authorization

Add automated tests

Add a frontend UI (React or simple HTML)



These are foundational concepts used in real-world backend and cloud-native systems.

👤 Author
Raphael Udubra
Computer Science student with interests in backend systems, containers, and distributed applications.
