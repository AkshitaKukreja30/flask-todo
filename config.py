import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
CORS_HEADERS = 'Content-Type'
SQLALCHEMY_TRACK_MODIFICATIONS = False