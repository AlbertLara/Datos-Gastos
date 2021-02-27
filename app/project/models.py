from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .db import db
from datetime import datetime

class Datos(db.Model):
    __tablename__ = "Datos"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    concepto = db.Column(db.String(255), nullable=False)
    dia = db.Column(db.DateTime, nullable=False)
    dinero = db.Column(db.Float, nullable=False)
    id_ingreso = db.Column(db.ForeignKey("Cuentas.id"), nullable=False)
    id_gasto= db.Column(db.ForeignKey("Cuentas.id"), nullable=False)

    @property
    def day(self):
        return self.dia.strftime('%Y-%m-%d')

    @property
    def ingreso(self):
      id = int(str(self.idtransaction).split("-")[1])
      nombre = ""
      if id > 0:
          cuenta = Cuentas.query.filter_by(id=id).first()
          nombre = "" if cuenta is None else cuenta.nombre
      return nombre

class Cuentas(db.Model):
    __tablename__ = "Cuentas"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    inicial = db.Column(db.Float, nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('La contraseña no es un atributo legible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Gastos(db.Model):
    __tablename__ = "Gastos"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    concepto = db.Column(db.String(255), nullable=False)
    mes = db.Column(db.DateTime, nullable=False)
    importe = db.Column(db.Float, nullable=False)
    num = db.Column(db.Integer, default=0)
