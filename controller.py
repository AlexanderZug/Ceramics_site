import re

from flask import flash, redirect, render_template, request

import mail_sender
import models
from app import app, db
from person_data import TELEGRAM, VK, WHATS_UP

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    When GET returns the main page.
    When POST performs validation,
    if the validation passes,
    then writes the data to the database and sends an email.
    """
    bio = models.MainPage.query.all()
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
    return render_template('index.html', bio=bio, telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/arts', methods=['GET'])
def arts():
    """Route to main page of painting. Only GET."""
    return render_template('arts.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/ceramics', methods=['GET'])
def ceramics():
    """Route to main page of ceramics. Only GET."""
    return render_template('ceramics.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/unclear', methods=['GET'])
def unclear_project():
    """Route to one of the painting page. Only GET."""
    return render_template('unclear_priject.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/blue', methods=['GET'])
def blue_project():
    """Route to one of the painting page. Only GET."""
    return render_template('blue_project.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/spring', methods=['GET'])
def spring():
    """Route to one of the painting page. Only GET."""
    return render_template('spring_project.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/fear', methods=['GET'])
def fear():
    """Route to one of the painting page. Only GET."""
    return render_template('fear.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/graphic', methods=['GET'])
def graphic():
    """Route to graphic page. Only GET."""
    return render_template('graphic.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/self_portrait', methods=['GET'])
def self_portrait():
    """Route to one of the projects page. Only GET."""
    return render_template('self_portrait.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/isolation', methods=['GET'])
def isolation():
    """Route to one of the projects page. Only GET."""
    return render_template('isolation.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/non_intensity', methods=['GET'])
def non_intensity():
    """Route to one of the projects page. Only GET."""
    return render_template('non_intensity.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)


@app.route('/loneliness', methods=['GET'])
def loneliness():
    """Route to one of the projects page. Only GET."""
    return render_template('loneliness.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK)
