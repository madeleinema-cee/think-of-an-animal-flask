from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import data_required, length
from flaskgame.user_answers import user_answers


class AnimalForm(FlaskForm):
    animal_name = StringField("Animal Name",
                              validators=[data_required(), length(min=2, max=20)])
    hair = RadioField('hair', choices=[('1', 'Yes'), ('0', 'No')])
    feathers = RadioField('feathers', choices=[('1', 'Yes'), ('0', 'No')])
    eggs = RadioField('eggs', choices=[('1', 'Yes'), ('0', 'No')])
    milk = RadioField('milk', choices=[('1', 'Yes'), ('0', 'No')])
    airborne = RadioField('airborne', choices=[('1', 'Yes'), ('0', 'No')])
    aquatic = RadioField('aquatic', choices=[('1', 'Yes'), ('0', 'No')])
    predator = RadioField('predator', choices=[('1', 'Yes'), ('0', 'No')])
    toothed = RadioField('toothed', choices=[('1', 'Yes'), ('0', 'No')])
    backbone = RadioField('backbone', choices=[('1', 'Yes'), ('0', 'No')])
    breathes = RadioField('breathes', choices=[('1', 'Yes'), ('0', 'No')])
    venomous = RadioField('venomous', choices=[('1', 'Yes'), ('0', 'No')])
    fins = RadioField('fins', choices=[('1', 'Yes'), ('0', 'No')])
    legs = RadioField('legs', choices=[('0', 'None'), ('2', '2'), ('4', '4'), ('5', '5'),
                                        ('6', '6'), ('8', '8')])
    tail = RadioField('tail', choices=[('1', 'Yes'), ('0', 'No')])
    domestic = RadioField('domestic', choices=[('1', 'Yes'), ('0', 'No')])
    catsize = RadioField('catsize', choices=[('1', 'Yes'), ('0', 'No')])
    class_type = RadioField('class type', choices=[('1', 'Mammal'), ('2', 'Bird'),
                                                    ('3', 'Reptile'), ('4', 'Fish'),
                                                    ('5', 'Amphibian'), ('6', 'Bug'),
                                                    ('7', 'Invertebrate')])
    submit = SubmitField('Submit')
