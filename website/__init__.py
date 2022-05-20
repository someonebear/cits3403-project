from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config.from_object("config.DevelopmentConfig")
  db.init_app(app)

  from .auth import auth
  from .views import views

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")

  from .models import User, Questions

  create_database(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
    
  return app

def create_database(app):
  if not path.exists('website/' + DB_NAME):
    db.create_all(app=app)
    print("Created Database")