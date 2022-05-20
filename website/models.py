from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  username = db.Column(db.String(150))
  questions = db.relationship('Questions')
  stats = db.relationship('Stats', uselist=False)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def to_dict(self, include_email=False):
    data = {
      'id': self.id,
      'username': self.username
    }
    if include_email:
      data['email'] = self.email
    return data

  def from_dict(self, data, new_user=False):
    for field in ['username', 'email']:
      if field in data:
        setattr(self, field, data[field])
    if new_user and 'password' in data:
      self.set_password(data['password'])

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