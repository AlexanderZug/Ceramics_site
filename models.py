from datetime import datetime

from app import db


class Client(db.Model):
    """Class for sending data to the database."""

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(40))
    email: str = db.Column(db.String(40))
    message: str = db.Column(db.String(350))
    date: str = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name: str, email: str, message: str, date: str) -> None:
        self.name = name
        self.email = email
        self.message = message
        self.date = date


class MainPage(db.Model):
    """Class for edit index (biography and CV)."""

    id: int = db.Column(db.Integer, primary_key=True)
    biography_title: str = db.Column(db.String(200))
    education: str = db.Column(db.String(350))
    curriculum_vitae: str = db.Column(db.String(400))


db.create_all()