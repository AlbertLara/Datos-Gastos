from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, DateTimeField, DecimalField, SelectField
from wtforms.validators import DataRequired

class CreateRecord(FlaskForm):
    submit = SubmitField("Añadir registro")
    
    
class NewRecord(FlaskForm):
    concepto = StringField("Concepto", validators=[DataRequired()])
    dia = DateTimeField("Dia", validators=[DataRequired()])
    dinero = DecimalField("Dinero", validators=[DataRequired()])
    submit = SubmitField("Añadir")
    