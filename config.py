import os
from os.path import dirname, join, realpath

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Class with configurations."""

    SECRET_KEY: str = os.urandom(20)
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///website.db'
    SESSION_TYPE: str = 'sqlalchemy'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_PORT: int = 465
    MAIL_USE_SSL: bool = True
    MAIL_USERNAME: str = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD: str = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER: str = os.getenv('MAIL_DEFAULT_SENDER')
    SECURITY_PASSWORD_SALT: str = os.getenv('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH: str = 'sha512_crypt'
    BABEL_DEFAULT_LOCALE: str = 'ru'
    UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH: int = 8 * 1024 * 1024
    DEBUG: bool = True
