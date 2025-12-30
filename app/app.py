from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Example: postgresql://user:pass@db:5432/mydb
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), nullable=False)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.get("/tasks")
    def list_tasks():
        tasks = Task.query.all()
        return jsonify([{"id": t.id, "title": t.title} for t in tasks])

    @app.post("/tasks")
    def add_task():
        data = request.get_json(force=True)
        title = data.get("title", "").strip()
        if not title:
            return {"error": "title is required"}, 400
        t = Task(title=title)
        db.session.add(t)
        db.session.commit()
        return {"id": t.id, "title": t.title}, 201

    # Create tables on startup (simple approach for a small project)
    with app.app_context():
        db.create_all()

    return app

app = create_app()
