from flask import Flask, request, flash, redirect, render_template
import re

from person_data import TELEGRAM, WHATS_UP, VK_PAGE

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eiwbi8839183y84iuqh39731hx'

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['POST', 'GET'])
def base():
    if request.method == 'POST':
        rec = request.form
        name = rec.get('name')
        email = rec.get('email')
        message = rec.get('message')
        if len(name) < 2:
            flash('Your name must be at least 3 characters in length')
        elif not re.fullmatch(regex, email):
            flash("Your e-mail isn't correct.")
        else:
            flash('Your message sent.')
    return render_template('base.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


if __name__ == '__main__':
    from errors import *

    app.run(debug=True, host='0.0.0.0', port=5001)
