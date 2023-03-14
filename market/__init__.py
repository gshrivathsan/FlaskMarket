from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db?check_same_thread=False'
#postgresql://market_i6uh_user:RSER30J3ylc0YL8ha5WetRqHCL7C9Vof@dpg-cg7s30ndvk4ljrn3b22g-a/market_i6uh
app.config['SECRET_KEY'] = '81117add8ab027690bd40297'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category="info"

from market import routes
