import re

import sentry_sdk
from flask import Flask, flash, render_template, request, redirect
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from sentry_sdk.integrations.flask import FlaskIntegration


import models

import mail_sender
from config import Config


app = Flask(__name__)
sentry_sdk.init(
    dsn="https://2cee952aa4f245f786a29a41ac6183d8@o1204683.ingest.sentry.io/6346581",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
app.config.from_object(Config)
db = SQLAlchemy(app)
mail = Mail(app)
toastr = Toastr(app)
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['POST', 'GET'])
def index():
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
            client = models.Client(rec.get('name'), rec.get('email'), rec.get('message'), rec.get('date'))
            db.session.add(client)
            db.session.commit()
            mail_sender.Mail(rec.get('name'), rec.get('email'), rec.get('message')).send_message()
            return redirect('/')
    return render_template('index.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/arts', methods=['GET'])
def arts():
    """Route to painting page. Only GET."""
    return render_template('arts.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/ceramics', methods=['GET'])
def ceramics():
    """Route to ceramics page. Only GET."""
    return render_template('ceramics.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/unclear', methods=['GET'])
def unclear_project():
    """Route to painting page. Only GET."""
    return render_template('unclear_priject.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/blue', methods=['GET'])
def blue_project():
    """Route to painting page. Only GET."""
    return render_template('blue_project.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/spring', methods=['GET'])
def spring():
    """Route to painting page. Only GET."""
    return render_template('spring_project.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/fear', methods=['GET'])
def fear():
    """Route to painting page. Only GET."""
    return render_template('fear.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/graphic', methods=['GET'])
def graphic():
    """Route to painting page. Only GET."""
    return render_template('graphic.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/self_portrait', methods=['GET'])
def self_portrait():
    """Route to painting page. Only GET."""
    return render_template('self_portrait.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/isolation', methods=['GET'])
def isolation():
    """Route to painting page. Only GET."""
    return render_template('isolation.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/non_intensity', methods=['GET'])
def non_intensity():
    """Route to painting page. Only GET."""
    return render_template('non_intensity.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


@app.route('/loneliness', methods=['GET'])
def loneliness():
    """Route to painting page. Only GET."""
    return render_template('loneliness.html', telegram='https://t.me/sveta_pokrovskaya',
                           whats_up='https://api.whatsapp.com/send/?phone=79852568280',
                           vk_page='https://vk.com/id3404775')


if __name__ == '__main__':
    from errors import *
    import models

    app.run(debug=True, host='0.0.0.0', port=5001)
