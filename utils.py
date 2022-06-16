import os

from flask import request
from werkzeug.utils import secure_filename

import models
from app import app


def all_db_data_for_arts():
    bd_disc = models.ArtsPage.query.all()
    return bd_disc


def img_handler():
    filepath = secure_filename(request.files['image'].filename)
    image = request.files['image']
    image.save(os.path.join(app.config['UPLOADS_PATH'],
                            secure_filename(image.filename)))
    return filepath


def post_handler_for_arts():
    try:
        check_img = request.files['image'].filename != ''
    except AttributeError:
        check_img = True
    return check_img
