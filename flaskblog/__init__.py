from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class = Base)


# configuring flask_sqlalchemy extension to flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = '9990d8899c6d84c523797eeafc2852ba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

    # Create the application context
with app.app_context():
    # Create all tables defined in the models
    db.create_all()


from flaskblog import routes    

