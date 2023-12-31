from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity, replace with your preferred database

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from app import routes  # Import routes at the end to avoid circular imports
