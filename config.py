from person_data import DB_CONFIG, SECRET_KEY_FLASK, EMAIL, PASSWORD


class Config:
    """Class with configurations."""

    SECRET_KEY: str = SECRET_KEY_FLASK
    SQLALCHEMY_DATABASE_URI: str = DB_CONFIG
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_PORT: int = 465
    MAIL_USE_SSL: bool = True
    MAIL_USERNAME: str = EMAIL
    MAIL_PASSWORD: str = PASSWORD
    MAIL_DEFAULT_SENDER: str = EMAIL