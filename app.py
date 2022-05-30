import sentry_sdk
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from sentry_sdk.integrations.flask import FlaskIntegration

from config import Config

app = Flask(__name__)
sentry_sdk.init(
    dsn="https://d5b6d50e80b1481bad2cd5ad48cba935@o1204683.ingest.sentry.io/6416499",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
moment = Moment(app)
toastr = Toastr(app)

if __name__ == '__main__':
    import admin
    import controller
    from errors import *

    app.run(debug=True, host='0.0.0.0', port=5001)

