from datetime import datetime

from flask_security import RoleMixin, UserMixin

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


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class User(db.Model, UserMixin):
    """User-model for flask-admin."""

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(40))
    password: str = db.Column(db.String(40))
    active: bool = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    """Role-model for flask-admin."""

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True)


class MainPage(db.Model):
    """Class for edit index (biography and CV)."""

    id: int = db.Column(db.Integer, primary_key=True)
    biography_title: str = db.Column(db.String(200))
    education: str = db.Column(db.String(350))
    curriculum_vitae: str = db.Column(db.String(400))


class Graphic(db.Model):
    """Class for edit graphic (description, prise_and_size, image)."""

    id: int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.String(400))
    prise_and_size: str = db.Column(db.String(100))
    image: str = db.Column(db.Text, nullable=True, default='img/new_img/img43.jpg')


db.create_all()
