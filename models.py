from datetime import datetime

from flask_security import RoleMixin, UserMixin

from app import db


class IdModel(db.Model):
    """Class for creating abstract model with id-field."""
    __abstract__ = True

    id: int = db.Column(db.Integer, primary_key=True)


class Client(IdModel):
    """Class for sending data to the database."""

    name: str = db.Column(db.String(40))
    email: str = db.Column(db.String(40))
    message: str = db.Column(db.String(350))
    date: str = db.Column(db.DateTime, default=datetime.utcnow)


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class User(IdModel, UserMixin):
    """User-model for flask-admin."""

    email: str = db.Column(db.String(40))
    password: str = db.Column(db.String(40))
    active: bool = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(IdModel, RoleMixin):
    """Role-model for flask-admin."""

    name: str = db.Column(db.String(100), unique=True)


class MainPage(IdModel):
    """Class for edit index (biography and CV)."""

    biography_title: str = db.Column(db.String(200))
    education: str = db.Column(db.String(350))
    curriculum_vitae: str = db.Column(db.String(400))


class Graphic(IdModel):
    """Class for edit graphic (description, prise_and_size, image)."""

    description: str = db.Column(db.String(400))
    prise_and_size: str = db.Column(db.String(100))
    image: str = db.Column(db.Text, nullable=True, default='')


class ArtsPage(IdModel):
    """Class for edit arts (description, image)."""

    description_fear: str = db.Column(db.String(800))
    description_blue: str = db.Column(db.String(800))
    description_unclear: str = db.Column(db.String(800))
    image_fear: str = db.Column(db.Text, nullable=True)
    image_blue: str = db.Column(db.Text, nullable=True)
    image_unclear: str = db.Column(db.Text, nullable=True)


class CeramicPage(IdModel):
    """Class for edit ceramic (description, image)."""

    image_isolation: str = db.Column(db.Text, nullable=True)
    image_loneliness: str = db.Column(db.Text, nullable=True)
    image_non_intensity: str = db.Column(db.Text, nullable=True)
    image_self_portrait: str = db.Column(db.Text, nullable=True)


db.create_all()
