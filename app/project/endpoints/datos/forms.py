from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class DocumentToLoad(FlaskForm):
  document = FileField('Document', validators=[FileRequired(), FileAllowed(['xls', 'xlsx'], 'Excel Document only!')])