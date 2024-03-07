from propiedades.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contratos"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4)
    fechaCreacion = db.Column(db.DateTime)
    tipoContrato = db.Column(db.String)
    fechaTerminacion = db.Column(db.DateTime)
    pago = db.relationship('Pago')

class Pago(db.Model):
    __tablename__ = "pagos"
    contratoId = Column(db.String, ForeignKey("contratos.id"), primary_key=True)
