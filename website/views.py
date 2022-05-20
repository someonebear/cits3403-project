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
  user_stats = Stats.query.filter_by(user_id=current_user.id).first()
  stat_dict = {}
  for subject in ['psyc', 'hb', 'cs', 'econ']:
    subject_correct = subject + "_correct"
    subject_total = subject + "_total"
    if getattr(user_stats, subject_total) > 0:
      pct_correct = subject_correct / subject_total
      pct_correct = round(pct_correct, 2)
    else: 
      pct_correct = 0
    subject_pct = subject + "_percent"
    stat_dict[subject_pct] = str(pct_correct) + "%"
  return render_template("stats.html", user=current_user, stat_dict=stat_dict)