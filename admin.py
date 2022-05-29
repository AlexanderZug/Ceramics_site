from flask_admin import Admin
from app import app, db
from models import Client, MainPage
from flask_admin.contrib.sqla import ModelView

admin = Admin(app)
admin.add_view(ModelView(Client, db.session))
admin.add_view(ModelView(MainPage, db.session))