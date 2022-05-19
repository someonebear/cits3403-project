from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
  return render_template("quizzle.html", user=current_user)

@views.route('stats')
@login_required
def stats():
  return render_template("stats.html", user=current_user)