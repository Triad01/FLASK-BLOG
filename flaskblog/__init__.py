import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail




class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class = Base)


# configuring flask_sqlalchemy extension to flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = '9990d8899c6d84c523797eeafc2852ba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_USER')
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PASSWORD')
mail = Mail(app)




    # Create the application context
with app.app_context():
    # Create all tables defined in the models
    from flaskblog import models
    db.create_all()


from flaskblog import routes    

