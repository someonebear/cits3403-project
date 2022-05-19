from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User, Stats

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
  return render_template("quizzle.html", user=current_user)

@views.route('stats')
@login_required
def stats():
  user_id = current_user.id
  test_stat = Stats(user_id=user_id, hb_correct=2)
  db.session.add(test_stat)
  db.session.commit()
  user_stats = Stats.query.filter_by(user_id=user_id).first()
  hb_correct = user_stats.hb_correct
  return render_template("stats.html", user=current_user, hb_correct=hb_correct)