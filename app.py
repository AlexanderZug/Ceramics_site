from flask import Flask, render_template, url_for
from person_data import TELEGRAM, WHATS_UP, VK_PAGE


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


@app.route('/about')
def about():
    return render_template('about.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


@app.route('/contact')
def contact():
    return render_template('contact.html', telegram=TELEGRAM, whats_up=WHATS_UP, vk_page=VK_PAGE)


if __name__ == '__main__':
    app.run(debug=True)
