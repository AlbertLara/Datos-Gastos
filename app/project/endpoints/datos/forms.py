from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class CreateRecord(FlaskForm):
    submit = SubmitField("Añadir registro")

class NewRecord(FlaskForm):
    concepto = StringField("Concepto", validators=[DataRequired()], id="concepto")
    dia = DateField("Dia", validators=[DataRequired()])
    dinero = DecimalField("Dinero", validators=[DataRequired()])
    idtransaction = SelectField("Id Transaccion", validate_choice=False)
    submit = SubmitField("Añadir")