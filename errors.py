from flask import render_template

from app import application


@application.errorhandler(404)
def error404(error):
    return render_template('errors/404.html'), 404


@application.errorhandler(500)
def error500(error):
    return render_template('errors/500.html'), 500
