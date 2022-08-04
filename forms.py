from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class registerCity(FlaskForm):
    nombreCiudad = StringField('Name of the city:',validators=[InputRequired()])
    submit = SubmitField('Submit')