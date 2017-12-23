from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
from .qasi.util.gallery import Gallery

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

gallery = Gallery(os.path.dirname(__file__)+"/static/flexible/", 2, 20)

from app.qasi.controller import qasi

app.register_blueprint(qasi)
