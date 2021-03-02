from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, DecimalField, SelectField
from wtforms.validators import DataRequired

class CreateRecord(FlaskForm):
    submit = SubmitField("Añadir registro")

class NewRecord(FlaskForm):
    concepto = StringField("Concepto", validators=[DataRequired()], id="concepto")
    dia = DateTimeField("Dia", validators=[DataRequired()])
    dinero = DecimalField("Dinero", validators=[DataRequired()])
    tipo = SelectField("Tipo",choices=[("transact","Transaccion"), ("ingreso","Ingreso"), ("gasto","Gasto")],id="tipo")
    origen = SelectField("Origen", coerce=int)
    destino = SelectField("Destino", coerce=int)
    submit = SubmitField("Añadir")