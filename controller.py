import os
import re

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request

import mail_sender
import models
from app import application, captcha, db
from utils import all_db_data_for_arts, img_handler, post_handler_for_arts

load_dotenv()
# Regular expression that the user introduced an email
regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
)


@application.route('/', methods=['POST', 'GET'])
def index():
    """
    When GET returns the main page.
    When POST performs validation,
    if the validation passes,
    then writes the data to DB and sends an email.
    """
    bio = models.MainPage.query.all()
    if request.method == 'GET':
        return render_template(
            'index.html',
            bio=bio,
            telegram=os.getenv('TELEGRAM'),
            whats_up=os.getenv('WHATS_UP'),
            vk_page=os.getenv('VK'),
        )
    rec = request.form
    if captcha.validate():
        if len(rec.get('name')) < 2:
            flash('Your name must be at least 3 characters in length', 'error')
        elif not re.fullmatch(regex, rec.get('email')):
            flash("Your e-mail isn't correct.", 'error')
        else:
            flash('Your message sent.', 'success')
            client = models.Client(
                name=rec.get('name'),
                email=rec.get('email'),
                message=rec.get('message'),
                date=rec.get('date'),
            )
            db.session.add(client)
            db.session.commit()
            mail_sender.Mail(
                rec.get('name'), rec.get('email'), rec.get('message')
            ).send_message()
            return redirect('/')
    flash('Captcha incorrect.', 'error')
    return redirect('/')


@application.route('/arts', methods=['GET'])
def arts():
    """Route to main page of painting. Only GET."""
    return render_template(
        'arts.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
    )


@application.route('/ceramics', methods=['GET'])
def ceramics():
    """Route to main page of ceramics. Only GET."""
    return render_template(
        'ceramics.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
    )


@application.route('/unclear', methods=['GET', 'POST'])
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
    return render_template(
        'unclear_priject.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[0],
        unclear='unclear',
    )


@application.route('/blue', methods=['GET', 'POST'])
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
    return render_template(
        'blue_project.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[0],
        blue='blue',
    )


@application.route('/fear', methods=['GET', 'POST'])
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
    return render_template(
        'fear.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[0],
    )


@application.route('/graphic_page', methods=['GET', 'POST'])
def graphic_page():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    bd_foto_prise = models.Graphic.query.all()
    if request.method == 'POST':
        try:
            last_img = models.Graphic.query.order_by(
                models.Graphic.id.desc()
            ).first()
        except AttributeError:
            last_img = True
        if last_img:
            graphic = models.Graphic(image=img_handler())
            db.session.add(graphic)
            db.session.commit()
    return render_template(
        'graphic_page.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_foto_prise=bd_foto_prise,
    )


@application.route('/self_portrait', methods=['GET', 'POST'])
def self_portrait():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            self_portrait_img = models.CeramicPage(
                image_self_portrait=img_handler()
            )
            db.session.add(self_portrait_img)
            db.session.commit()
    return render_template(
        'self_portrait.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[1],
        self_portrait='self_portrait',
    )


@application.route('/isolation', methods=['GET', 'POST'])
def isolation():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            image_isolation_img = models.CeramicPage(
                image_isolation=img_handler()
            )
            db.session.add(image_isolation_img)
            db.session.commit()
    return render_template(
        'isolation.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[1],
        isolation='isolation',
    )


@application.route('/non_intensity', methods=['GET', 'POST'])
def non_intensity():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            image_non_intensity = models.CeramicPage(
                image_non_intensity=img_handler()
            )
            db.session.add(image_non_intensity)
            db.session.commit()
    return render_template(
        'non_intensity.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[1],
        non_intensity='non_intensity',
    )


@application.route('/loneliness', methods=['GET', 'POST'])
def loneliness():
    """
    When GET returns the graphic page.
    When POST accepts the photo, saves in the download folder;
    the path to photography is recorded in the DB.
    """
    if request.method == 'POST':
        if post_handler_for_arts():
            image_loneliness = models.CeramicPage(
                image_loneliness=img_handler()
            )
            db.session.add(image_loneliness)
            db.session.commit()
    return render_template(
        'loneliness.html',
        telegram=os.getenv('TELEGRAM'),
        whats_up=os.getenv('WHATS_UP'),
        vk_page=os.getenv('VK'),
        bd_content=all_db_data_for_arts()[1],
        loneliness='loneliness',
    )
