from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150), nullable=False)
    chats = db.relationship('Chat', backref='user', passive_deletes=True)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Text, nullable=False)
    chatlog = db.Column(db.String)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    student = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)