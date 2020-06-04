from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, length


class AnimalForm(FlaskForm):
    animal_name = StringField("Animal Name",
                              validators=[data_required(), length(min=2, max=20)])
    submit = SubmitField('Submit')
