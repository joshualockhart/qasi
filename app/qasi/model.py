from flask import Flask
import os
from .. import db
from flask_sqlalchemy import SQLAlchemy
from .util.image_data import ImageData

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(1024), unique=True, nullable=False)
    annotations = db.relationship('Annotation', backref='annotationowner',lazy=True)

    def add_annotation(self, annotation):
        if isinstance(annotation, Annotation):
            self.annotations.append(annotation)
        else:
            raise(TypeError("Attempted to add non-annotation to an image"))

    def get_labelled_subimages(self):
        subimages = []
        labels = []
        for annotation in self.annotations:
            current_dir = os.path.dirname(__file__)
            data = ImageData(current_dir+'/../static/flexible/'+self.filename)
            label = annotation.label
            x = annotation.x
            y = annotation.y
            w = annotation.w
            h = annotation.h

            subimage_data = data.get_subimage(x,y,w,h)
            subimages.append(subimage_data)
            labels.append(label)
        return subimages, labels

class Annotation(db.Model):
    __tablename__ = 'annotations'
    id = db.Column(db.Integer, primary_key = True)

    label = db.Column(db.String(1024), nullable=False)

    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    w = db.Column(db.Float, nullable=False)
    h = db.Column(db.Float, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    def toJSON(self):
        return {'label':self.label,
                'x':self.x,
                'y':self.y,
                'w':self.w,
                'h':self.h
                }
