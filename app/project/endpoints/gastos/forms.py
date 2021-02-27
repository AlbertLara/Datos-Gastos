from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

class Create(FlaskForm):
  submit = SubmitField('Crear cuenta')