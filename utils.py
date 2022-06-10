import os

from flask import request
from werkzeug.utils import secure_filename

from app import app


def img_handler():
    filepath = secure_filename(request.files['image'].filename)
    image = request.files['image']
    image.save(os.path.join(app.config['UPLOADS_PATH'],
                            secure_filename(image.filename)))
    return filepath
