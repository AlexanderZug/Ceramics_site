import os

from flask import request
from werkzeug.utils import secure_filename

import models
from app import application


def all_db_data_for_arts():
    """Function gets all query for arts and ceramic from DB."""
    bd_content_arts = models.ArtsPage.query.all()
    bd_content_ceramic = models.CeramicPage.query.all()
    return bd_content_arts, bd_content_ceramic


def img_handler():
    """Function has path to upload directory."""
    filepath = secure_filename(request.files['image'].filename)
    image = request.files['image']
    image.save(os.path.join(application.config['UPLOADS_PATH'],
                            secure_filename(image.filename)))
    return filepath


def post_handler_for_arts():
    """
    Function checks if the foto was uploaded and
    returns true if the DB is empty to avoid error.
    """
    try:
        check_img = request.files['image'].filename != ''
    except AttributeError:
        check_img = True
    return check_img
