import re

import sentry_sdk
from flask import Flask, flash, render_template, request
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from sentry_sdk.integrations.flask import FlaskIntegration

import mail_sender
import models
from config import Config
from person_data import PATH_TO_SENTRY_LOG, TELEGRAM, VK_PAGE, WHATS_UP

app = Flask(__name__)
sentry_sdk.init(
    dsn=PATH_TO_SENTRY_LOG,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
app.config.from_object(Config)
db = SQLAlchemy(app)
mail = Mail(app)
toastr = Toastr(app)
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['POST', 'GET'])
def base():
    """
    When GET returns the main page.
    When POST performs validation,
    if the validation passes,
    then writes the data to the database and sends an email.
    """
    if request.method == 'POST':
        rec = request.form
        if len(rec.get('name')) < 2:
            flash('Your name must be at least 3 characters in length', 'error')
        elif not re.fullmatch(regex, rec.get('email')):
            flash("Your e-mail isn't correct.", 'error')
        else:
            flash('Your message sent.', 'success')
            client = models.Client(rec.get('name'), rec.get('email'), rec.get('message'))
            db.session.add(client)
            db.session.commit()
            mail_sender.Mail(rec.get('name'), rec.get('email'), rec.get('message')).send_message()
    return render_template('base.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


@app.route('/arts', methods=['GET'])
def arts():
    """Route to painting page. Only GET."""
    return render_template('arts.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


@app.route('/ceramics', methods=['GET'])
def ceramics():
    """Route to ceramics page. Only GET."""
    return render_template('ceramics.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


if __name__ == '__main__':
    from errors import *

    app.run(debug=True, host='0.0.0.0', port=5001)
