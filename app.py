from flask import Flask, request, flash, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import re

import models
from config import Config
from person_data import TELEGRAM, WHATS_UP, VK_PAGE

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['POST', 'GET'])
def base():
    if request.method == 'POST':
        rec = request.form
        if len(rec.get('name')) < 2:
            flash('Your name must be at least 3 characters in length', category='danger')
        elif not re.fullmatch(regex, rec.get('email')):
            flash("Your e-mail isn't correct.", category='danger')
        else:
            flash('Your message sent.', category='success')
            client = models.Client(rec.get('name'), rec.get('email'), rec.get('message'))
            db.session.add(client)
            db.session.commit()
    return render_template('base.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


if __name__ == '__main__':
    from errors import *

    app.run(debug=True, host='0.0.0.0', port=5001)
