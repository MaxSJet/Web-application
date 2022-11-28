from flask import Blueprint, request, jsonify
import os
from flask import Flask, flash, request, redirect, url_for
from app import db, app
from ..models.base import Dish
from flask_cors import CORS, cross_origin

mod = Blueprint('dishes', __name__, url_prefix='/dishes')
CORS(mod)


@mod.route('/', methods=['GET'])
@cross_origin()
def get_all():
    dishes = Dish.query.all()

    return jsonify(dishes)


@mod.route('/<int:dish_id>', methods=['GET'])
@cross_origin()
def get_by_id(dish_id):
    dish = Dish.query.filter_by(id=dish_id).first_or_404()
    return jsonify(dish)


@mod.route('/', methods=['POST'])
@cross_origin()
def create():
    file = request.files.get('image_url',  '')
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    dish = Dish(
        cost=request.form['cost'],
        name=request.form['name'],
        weight=request.form['weight'],
        compound=request.form['compound'],
        image_url=f"/static/{file.filename}"
    )

    db.session.add(dish)
    db.session.commit()

    return '', 204


@mod.route('/<int:dish_id>', methods=['PATCH'])
@cross_origin()
def update(dish_id):
    dish = Dish.query.filter_by(id=dish_id).first_or_404()

    file = request.files.get('image_url',  '')
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    dish.cost = request.json['cost']
    dish.name = request.json['name']
    dish.weight = request.json['weight']
    dish.compound = request.json['compound']
    dish.image_url = file

    db.session.add(dish)
    db.session.commit()

    return '', 204


@mod.route('/<int:dish_id>', methods=['DELETE'])
@cross_origin()
def delete(dish_id):
    dish = Dish.query.filter_by(id=dish_id).first_or_404()

    db.session.delete(dish)
    db.session.commit()
    return '', 204
