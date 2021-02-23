from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()



class Datos(db.Model):
  __tablename__="Datos"
  id = db.Column(db.Integer, primary_key=True,nullable=False)
  concepto = db.Column(db.String(255),nullable=False)
  dia = db.Column(db.DateTime,nullable=False)
  dinero = db.Column(db.Float,nullable=False)
  idtransaction = db.Column(db.String(3),nullable=False)
  
class Cuentas(db.Model):
  __tablename__="Cuentas"
  id = db.Column(db.Integer, primary_key=True,nullable=False)
  nombre = db.Column(db.String(255),nullable=False)
  inicial = db.Column(db.Float,nullable=False)
  
class User(UserMixin, db.Model):
  pass