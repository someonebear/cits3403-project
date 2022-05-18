from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
  data = request.form
  return render_template("login.html", boolean=True)

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
  if request.method == "POST":
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    if len(email) < 4:
      flash("Email must be greater than 3 characters.", category="error")
    elif password1 != password2:
      flash("The passwords do not match.", category="error")
    elif len(password1) < 7:
      flash("Password must be longer than 6 characters.", category="error")
    else:
      flash("Account Created", category=success)
  return render_template("signup.html", boolean=True)