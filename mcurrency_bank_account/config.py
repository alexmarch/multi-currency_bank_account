import os

MYSQL_USER = os.environ.get('MYSQL_USER', '')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', '')
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@db/%s' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
