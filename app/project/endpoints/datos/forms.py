from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, DecimalField, SelectField
from wtforms.validators import DataRequired

class CreateRecord(FlaskForm):
    submit = SubmitField("Añadir registro")

class NewRecord(FlaskForm):
    concepto = StringField("Concepto", validators=[DataRequired()])
    dia = DateTimeField("Dia", validators=[DataRequired()])
    dinero = DecimalField("Dinero", validators=[DataRequired()])
    """tipo = SelectField("Tipo", choices=[("transferencia","Transferencia"), ("ingreso","Ingreso"), ("gasto","Gasto")], validators=[DataRequired()])
    ingreso = SelectField("Ingreso")
    gasto = SelectField("Gasto")"""
    idtransaction = SelectField("Id Transaccion")
    submit = SubmitField("Añadir")