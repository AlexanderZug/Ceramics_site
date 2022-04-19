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
