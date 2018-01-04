from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify, abort, make_response, redirect, url_for, Blueprint
#from .util.gallery import gallery
import os
import json

qasi = Blueprint('qasi', __name__, template_folder='templates')
from .. import db

from .model import *
from .. import gallery

gal = gallery

def get_image_by_filename(filename):
    image = Image.query.filter_by(filename=filename).first()
    if image == None:
        raise ValueError("No image with filename {}".format(filename))
    return image

def annotate_image(filename, label, x, y, w, h):
    try:
        annotation = Annotation(label=label, x=x, y=y, w=w, h=h)
        image = get_image_by_filename(filename)
        image.add_annotation(annotation)
        db.session.commit()
    except Exception as e: raise

@qasi.route('/process_images', methods=['GET'])
def process_images():
    output_directory = gal.root_directory+"/labelled_subimages/"
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    print("Saving annotated subimages to {}".format(output_directory))

    images = Image.query.all()
    i = 0
    for image in images:
        print("processing {}".format(image.filename))
        sub_images, labels = image.get_labelled_subimages()
        for (img,label) in zip(sub_images,labels):
            img.save(output_directory+"/"+str(label), str(i)+".png")
            i+=1
    return render_template("done.html")

@qasi.route('/gallery/<page_number>', methods=['GET'])
def gallery(page_number):
    page_number = int(page_number)
    images=gal.get_page(page_number)
    num_pages = gal.num_pages
    
    if page_number <= num_pages:
        return render_template("gallery.html",page_number=page_number,num_pages=num_pages,images=images)
    else:
        return not_found("Can't find that page")

@qasi.route('/', methods=['GET'])
def gallery_no_args():
    return gallery(1)

@qasi.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@qasi.route('/edit/<image_name>/update', methods=['POST'])
def update(image_name):
    if os.path.isfile(gal.root_directory+"/"+image_name):
        if request.is_json:
            image = get_image_by_filename(image_name)
            image.annotations = []
            db.session.add(image)
            db.session.commit()
            return edit(image_name)
        else:
            abort(400)
    else:
        return not_found("can't find that file")

@qasi.route('/edit/<image_name>', methods=['GET', 'POST'])
def edit(image_name):
    if os.path.isfile(gal.root_directory+"/"+image_name):
        try:
            image = get_image_by_filename(image_name)
        except ValueError:
            image = Image(filename=image_name, annotations = [])

        if request.method == 'POST':
            if request.is_json:
                content = request.get_json(silent=True)
                for annotation in content:
                    ann = Annotation(label = annotation['label'],
                                     x = annotation['x'],
                                     y = annotation['y'],
                                     w = annotation['w'],
                                     h = annotation['h']
                                     )

                    image.annotations.append(ann)

            else:
                abort(400)
        annotations = image.annotations
        db.session.add(image)
        db.session.commit()

        return render_template('index.html',image_name=image_name, annotations=json.dumps([ann.toJSON() for ann in image.annotations]))
    else:
        return not_found("can't find that file")
