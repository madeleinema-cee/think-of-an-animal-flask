from flaskgame import db, app


class AnimalName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(20), nullable=False)
    hair = db.Column(db.Integer, nullable=False)
    feathers = db.Column(db.Integer, nullable=False)
    eggs = db.Column(db.Integer, nullable=False)
    milk = db.Column(db.Integer, nullable=False)
    airborne = db.Column(db.Integer, nullable=False)
    aquatic = db.Column(db.Integer, nullable=False)
    predator = db.Column(db.Integer, nullable=False)
    toothed = db.Column(db.Integer, nullable=False)
    backbone = db.Column(db.Integer, nullable=False)
    breathes = db.Column(db.Integer, nullable=False)
    venomous = db.Column(db.Integer, nullable=False)
    fins = db.Column(db.Integer, nullable=False)
    legs = db.Column(db.Integer, nullable=False)
    tail = db.Column(db.Integer, nullable=False)
    domestic = db.Column(db.Integer, nullable=False)
    catsize = db.Column(db.Integer, nullable=False)
    class_type = db.Column(db.Integer, nullable=False)

