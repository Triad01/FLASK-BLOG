import json
from flaskblog import db, login_manager, app
from flask_login import UserMixin
from datetime import datetime, timedelta
from sqlalchemy.orm import Mapped, mapped_column
from itsdangerous.url_safe import URLSafeTimedSerializer




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(unique=True, nullable=False)
    email:Mapped[str] = mapped_column(unique=True, nullable=False)
    image_file:Mapped[str] = mapped_column(nullable=False, default='default.jpg')
    password:Mapped[str] = mapped_column(nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        SECRET_KEY = app.config["SECRET_KEY"]
        serializer = URLSafeTimedSerializer(SECRET_KEY, salt = "reset")
        expiration_time = (datetime.utcnow() + timedelta(seconds=expires_sec)).isoformat()
        payload = {"user_id": 1, "exp": expiration_time}
        json_payload = json.dumps(payload)
        token = serializer.dumps(json_payload)
        return token
    
    @staticmethod
    def verify_reset_token(token):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'], salt= "reset")
        try:
            user_id = serializer.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    






































    # class User(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship("Post", backref="author", lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
