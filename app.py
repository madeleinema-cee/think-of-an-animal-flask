from db import Db

db = Db('animals.db')

data = [
    ('assets/zoo.csv', 'animals'),
    ('assets/class.csv', 'classes')
]

db.setup(data)

