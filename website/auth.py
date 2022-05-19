from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Stats
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password1')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash("Successful log in!", category='success')
        login_user(user, remember=True)
        return redirect(url_for("views.home"))
      else:
        flash("Incorrect password. Try again.", category='error')
    else:
      flash("User does not exist.", category='error')

  return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
  if request.method == "POST":
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    user = User.query.filter_by(email=email).first()

    if user:
      flash("User already exists.", category="error")
    elif len(email) < 4:
      flash("Email must be greater than 3 characters.", category="error")
    elif password1 != password2:
      flash("The passwords do not match.", category="error")
    elif len(password1) < 7:
      flash("Password must be longer than 6 characters.", category="error")
    else:
      new_user = User(username=username, email=email, password=generate_password_hash(password1, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      flash("Account Created", category='success')
      login_user(new_user, remember=True)
      new_user_stat = Stats(user_id=new_user.id)
      db.session.add(new_user_stat)
      db.session.commit()
      return redirect(url_for("views.home"))
  return render_template("signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))