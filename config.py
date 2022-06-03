import os
from person_data import *


class Config:
    """Class with configurations."""

    SECRET_KEY: str = os.urandom(20)
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///website.db'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_PORT: int = 465
    MAIL_USE_SSL: bool = True
    MAIL_USERNAME: str = MAIL_USERNAME
    MAIL_PASSWORD: str = MAIL_PASSWORD
    MAIL_DEFAULT_SENDER: str = MAIL_DEFAULT_SENDER
    SECURITY_PASSWORD_SALT: str = SECURITY_PASSWORD_SALT
    SECURITY_PASSWORD_HASH: str = 'sha512_crypt'
    BABEL_DEFAULT_LOCALE: str = 'ru'
    UPLOAD_FOLDER: str = 'static/uploads/img/'
