from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  username = db.Column(db.String(150))
  questions = db.relationship('Questions')
  stats = db.relationship('Stats', uselist=False)

  def to_dict(self, include_email=False):
    data = {
      'id': self.id,
      'username': self.username,
      ''
    }

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
  hb_correct = db.Column(db.Integer, default=0)
  hb_total = db.Column(db.Integer, default=0)
  psyc_correct = db.Column(db.Integer, default=0)
  psyc_total = db.Column(db.Integer, default=0)
  cs_correct = db.Column(db.Integer, default=0)
  cs_total = db.Column(db.Integer, default=0)
  econ_correct = db.Column(db.Integer, default=0)
  econ_total = db.Column(db.Integer, default=0)