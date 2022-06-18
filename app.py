import sentry_sdk
from flask import Flask
from flask_babelex import Babel
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sessionstore import Session
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from sentry_sdk.integrations.flask import FlaskIntegration

from config import Config
from person_data import SENTRY

application = Flask(__name__)
sentry_sdk.init(
    dsn=SENTRY,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
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


if __name__ == '__main__':
    import admin
    import controller
    from errors import *

    application.run(debug=True, host='0.0.0.0', port=5001)
