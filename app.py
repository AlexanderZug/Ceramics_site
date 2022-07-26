import os

import sentry_sdk
from dotenv import load_dotenv
from flask import Flask
from flask_babelex import Babel
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_session_captcha import FlaskSessionCaptcha
from flask_sessionstore import Session
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from sentry_sdk.integrations.flask import FlaskIntegration

from config import Config

load_dotenv()

application = Flask(__name__)
sentry_sdk.init(
    dsn=os.getenv('SENTRY'),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
mail = Mail(application)
moment = Moment(application)
toastr = Toastr(application)
babel = Babel(application)
application.config['SESSION_SQLALCHEMY'] = db
Session(application)
captcha = FlaskSessionCaptcha(application)

if __name__ == '__main__':
    from admin import *
    from controller import *
    from errors import *

    application.run(host='0.0.0.0', port=5001)
