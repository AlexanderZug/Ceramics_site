import re

from flask import flash, redirect, render_template, request

import mail_sender
import models
from app import app, db
from person_data import TELEGRAM, VK, WHATS_UP
from utils import all_db_data_for_arts, img_handler, post_handler_for_arts

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    When GET returns the main page.
    When POST performs validation,
    if the validation passes,
    then writes the data to DB and sends an email.
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


@app.route('/unclear', methods=['GET', 'POST'])
def unclear_project():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            unclear_img = models.ArtsPage(image_unclear=img_handler())
            db.session.add(unclear_img)
            db.session.commit()
    return render_template('unclear_priject.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK, bd_content=all_db_data_for_arts()[0],
                           unclear='unclear')


@app.route('/blue', methods=['GET', 'POST'])
def blue_project():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            blue_img = models.ArtsPage(image_blue=img_handler())
            db.session.add(blue_img)
            db.session.commit()
    return render_template('blue_project.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK, bd_content=all_db_data_for_arts()[0],
                           blue='blue')


@app.route('/fear', methods=['GET', 'POST'])
def fear():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            fear_img = models.ArtsPage(image_fear=img_handler())
            db.session.add(fear_img)
            db.session.commit()
    return render_template('fear.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK, bd_content=all_db_data_for_arts()[0])


@app.route('/graphic_page', methods=['GET', 'POST'])
def graphic_page():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    bd_foto_prise = models.Graphic.query.all()
    if request.method == 'POST':
        try:
            last_img = models.Graphic.query.order_by(models.Graphic.id.desc()).first()
        except AttributeError:
            last_img = True
        if last_img:
            graphic = models.Graphic(image=img_handler())
            db.session.add(graphic)
            db.session.commit()
    return render_template('graphic_page.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK, bd_foto_prise=bd_foto_prise)


@app.route('/self_portrait', methods=['GET', 'POST'])
def self_portrait():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            self_portrait_img = models.CeramicPage(image_self_portrait=img_handler())
            db.session.add(self_portrait_img)
            db.session.commit()
    return render_template('self_portrait.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK,
                           bd_content=all_db_data_for_arts()[1])


@app.route('/isolation', methods=['GET', 'POST'])
def isolation():
    """Route to one of the projects page. Only GET."""
    if request.method == 'POST':
        if post_handler_for_arts():
            image_isolation_img = models.CeramicPage(image_isolation=img_handler())
            db.session.add(image_isolation_img)
            db.session.commit()
    return render_template('isolation.html', telegram=TELEGRAM,
                           whats_up=WHATS_UP,
                           vk_page=VK,
                           bd_content=all_db_data_for_arts()[1])


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
