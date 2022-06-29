from flask_wtf import FlaskForm, RecaptchaField


class ContactForm(FlaskForm):
    recaptcha = RecaptchaField()