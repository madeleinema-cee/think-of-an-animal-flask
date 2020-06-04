from flaskgame import db, app


class AnimalName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(20), unique=True, nullable=False)
