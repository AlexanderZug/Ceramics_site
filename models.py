from app import db


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(40))
    message = db.Column(db.String(150))

    def __init__(self, name: str, email: str, message: str):
        self.name = name
        self.email = email
        self.message = message
