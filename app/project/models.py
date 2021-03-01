from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .db import db
from datetime import datetime

class Datos(db.Model):
    __tablename__ = "Datos"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    concepto = db.Column(db.String(255), nullable=False)
    dia = db.Column(db.DateTime(""), nullable=False)
    dinero = db.Column(db.Float, nullable=False)
    id_ingreso = db.Column(db.ForeignKey("Cuentas.id"), nullable=False)
    id_gasto = db.Column(db.ForeignKey("Cuentas.id"), nullable=False)
    cuenta_ingreso = db.relationship("Cuentas", primaryjoin=lambda: Datos.id_ingreso == Cuentas.id)
    cuenta_gasto = db.relationship("Cuentas", primaryjoin=lambda: Datos.id_gasto == Cuentas.id)

    @property
    def day(self):
        return self.dia.strftime('%d/%m/%Y')

    @property
    def mes(self):
        return self.dia.strftime('%m/%Y')

class Cuentas(db.Model):
    __tablename__ = "Cuentas"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    inicial = db.Column(db.Float, nullable=False)
    gastos = db.relationship("Datos", primaryjoin=lambda: Cuentas.id == Datos.id_gasto)
    ingresos = db.relationship("Datos", primaryjoin=lambda: Cuentas.id == Datos.id_ingreso)


    @property
    def all_gastos(self):
        return round(sum([gasto.dinero for gasto in self.gastos]), 2)

    @property
    def all_ingresos(self):
        return round(sum([gasto.dinero for gasto in self.ingresos]), 2)

    @property
    def diff(self):
        return round(self.all_ingresos - self.all_gastos, 2)

    @property
    def total(self):
        total = round(self.diff + self.inicial, 2)
        return total


class Gastos(db.Model):
    __tablename__ = "Gastos"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    concepto = db.Column(db.String(255), nullable=False)
    mes = db.Column(db.DateTime, nullable=False)
    gasto_esperado =db.Column(db.Float, nullable=False)
    gasto_real = db.Column(db.Float, default=0)


    @property
    def month(self):
        month = self.mes.strftime("%m/%Y")
        return month


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
        
        
def get_cuentas_ids():
  cuentas = Cuentas.query.all()
  max_id = max([cuenta.id for cuenta in cuentas])+1
  ids = []
  for i in range(0,max_id):
    for j in range(0,max_id):
      if i != j:
        id = f"{i}-{j}"
        ids.append(id)
  return ids