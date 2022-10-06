from app import db
from dataclasses import dataclass


@dataclass
class Dish(db.Model):
    id: int
    name: str
    image_url: str
    weight: float
    cost: float
    compound: str

    __tablename__ = 'dishes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    image_url = db.Column(db.String(255))
    weight = db.Column(db.Float)
    cost = db.Column(db.Float)
    compound = db.Column(db.String(255))

    def __init__(self, name=None, image_url=None, weight=None, cost=None, compound=None):
        self.name = name
        self.image_url = image_url
        self.weight = weight
        self.cost = cost
        self.compound = compound

    def __repr__(self):
        return '<Dish %r>' % self.name
