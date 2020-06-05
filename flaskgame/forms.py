from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import data_required, length, input_required


class AnimalForm(FlaskForm):
    animal_name = StringField("Animal Name",
                              validators=[data_required(), length(min=2, max=20)])
    hair = SelectField('hair', choices=[('1', 'yes'), ('0', 'no')])
    feathers = SelectField('feathers', choices=[('1', 'yes'), ('0', 'no')])
    eggs = SelectField('eggs', choices=[('1', 'yes'), ('0', 'no')])
    milk = SelectField('milk', choices=[('1', 'yes'), ('0', 'no')])
    airborne = SelectField('airborne', choices=[('1', 'yes'), ('0', 'no')])
    aquatic = SelectField('aquatic', choices=[('1', 'yes'), ('0', 'no')])
    predator = SelectField('predator', choices=[('1', 'yes'), ('0', 'no')])
    toothed = SelectField('toothed', choices=[('1', 'yes'), ('0', 'no')])
    backbone = SelectField('backbone', choices=[('1', 'yes'), ('0', 'no')])
    breathes = SelectField('breathes', choices=[('1', 'yes'), ('0', 'no')])
    venomous = SelectField('venomous', choices=[('1', 'yes'), ('0', 'no')])
    fins = SelectField('fins', choices=[('1', 'yes'), ('0', 'no')])
    legs = SelectField('legs', choices=[('0', '0'), ('2', '2'), ('4', '4'), ('5', '5'),
                                        ('6', '6'), ('8', '8')])
    tail = SelectField('tail', choices=[('1', 'yes'), ('0', 'no')])
    domestic = SelectField('domestic', choices=[('1', 'yes'), ('0', 'no')])
    catsize = SelectField('catsize', choices=[('1', 'yes'), ('0', 'no')])
    class_type = SelectField('class_type', choices=[('1', 'mammal'), ('2', 'bird'),
                                                    ('3', 'reptile'), ('4', 'fish'),
                                                    ('5', 'amphibian'), ('6', 'bug'),
                                                    ('7', 'invertebrate')])
    submit = SubmitField('Submit')
