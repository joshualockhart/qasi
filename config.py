import os

class Config(object):
    DB_FILENAME=os.path.dirname(__file__)+'/app/static/flexible/qasi.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DB_FILENAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
