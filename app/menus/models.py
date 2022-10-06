from app import db
from dataclasses import dataclass
from datetime import date
from ..dishes.models import Dish

dishes = db.Table('menu_dishes',
                  db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id'), primary_key=True),
                  db.Column('menu_id', db.Integer, db.ForeignKey('menus.id'), primary_key=True)
                  )


@dataclass
class Menu(db.Model):
    id: int
    dishes: [Dish]
    date: db.Date

    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    dishes = db.relationship('Dish', secondary=dishes, lazy='subquery',
        backref=db.backref('menus', lazy=True))
    date = db.Column(db.Date)

    def __init__(self, dishes=None, date=None):
        self.dishes = dishes
        self.date = date

    def __repr__(self):
        return '<Menu>'
