from flask_admin import Admin
from flask_security import SQLAlchemySessionUserDatastore, Security, SQLAlchemyUserDatastore

from app import app, db
from models import Client, MainPage, Role, User
from flask_admin.contrib.sqla import ModelView

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


admin = Admin(app)
admin.add_view(ModelView(Client, db.session))
admin.add_view(ModelView(MainPage, db.session))