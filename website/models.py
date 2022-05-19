from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  username = db.Column(db.String(150))
  questions = db.relationship('Questions')

class Questions(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  subject = db.Column(db.String(150))
  question = db.Column(db.String(1000))
  answer = db.Column(db.Text(1000))
  alternate1 = db.Column(db.Text(1000))
  alternate2 = db.Column(db.Text(1000))
  alternate3 = db.Column(db.Text(1000))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Stats(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  hb_correct = db.Column(db.Integer)
  hb_total = db.Column(db.Integer)
  psyc_correct = db.Column(db.Integer)
  psyc_total = db.Column(db.Integer)
  cs_correct = db.Column(db.Integer)
  cs_total = db.Column(db.Integer)
  econ_correct = db.Column(db.Integer)
  econ_total = db.Column(db.Integer)