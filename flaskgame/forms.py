from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import data_required, length


class AnimalForm(FlaskForm):
    animal_name = StringField("Animal Name",
                              validators=[data_required(), length(min=2, max=20)])
    hair = RadioField('Hair', choices=[('1', 'Yes'), ('0', 'No')])
    feathers = RadioField('Feathers', choices=[('1', 'Yes'), ('0', 'No')])
    eggs = RadioField('Eggs', choices=[('1', 'Yes'), ('0', 'No')])
    milk = RadioField('Milk', choices=[('1', 'Yes'), ('0', 'No')])
    airborne = RadioField('Airborne', choices=[('1', 'Yes'), ('0', 'No')])
    aquatic = RadioField('Aquatic', choices=[('1', 'Yes'), ('0', 'No')])
    predator = RadioField('Predator', choices=[('1', 'Yes'), ('0', 'No')])
    toothed = RadioField('Toothed', choices=[('1', 'Yes'), ('0', 'No')])
    backbone = RadioField('Backbone', choices=[('1', 'Yes'), ('0', 'No')])
    breathes = RadioField('Breathes', choices=[('1', 'Yes'), ('0', 'No')])
    venomous = RadioField('Venomous', choices=[('1', 'Yes'), ('0', 'No')])
    fins = RadioField('Fins', choices=[('1', 'Yes'), ('0', 'No')])
    legs = RadioField('Legs', choices=[('0', 'None'), ('2', '2'), ('4', '4'), ('5', '5'),
                                        ('6', '6'), ('8', '8')])
    tail = RadioField('Tail', choices=[('1', 'Yes'), ('0', 'No')])
    domestic = RadioField('Domestic', choices=[('1', 'Yes'), ('0', 'No')])
    catsize = RadioField('Catsize', choices=[('1', 'Yes'), ('0', 'No')])
    class_type = RadioField('Class Type', choices=[('1', 'Mammal'), ('2', 'Bird'),
                                                    ('3', 'Reptile'), ('4', 'Fish'),
                                                    ('5', 'Amphibian'), ('6', 'Bug'),
                                                    ('7', 'Invertebrate')])
    submit = SubmitField('Submit')
