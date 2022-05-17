class Config:
    """Class with configurations."""

    SECRET_KEY: str = "hjfsjjbjvjjjjehbbannnsj"
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///website.db'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_PORT: int = 465
    MAIL_USE_SSL: bool = True
    MAIL_USERNAME: str = 'developer.unterwegs@gmail.com'
    MAIL_PASSWORD: str = 'jvowpupvmopkuchn'
    MAIL_DEFAULT_SENDER: str = 'developer.unterwegs@gmail.com'
