import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('config.py', silent=True)

db = SQLAlchemy(app)
socketio = SocketIO(app, manage_session=True)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# import models, socketio handlers
from models import *
from handlers import *
from controllers import dashboard, auth

app.register_blueprint(dashboard.bp, url_prefix='/')
app.register_blueprint(auth.bp, url_prefix='/auth')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=True)
