from flask import Flask, render_template, url_for
from person_data import TELEGRAM, WHATS_UP, VK_PAGE


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def base():
    return render_template('base.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


if __name__ == '__main__':
    from errors import *

    app.run(debug=True)
