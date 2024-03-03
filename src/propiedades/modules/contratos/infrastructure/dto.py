from propiedades.config.db import db
from enum import Enum
from propiedades.modules.contratos.domain.value_objects import TiposContrato, TipoMoneda, TipoMetodoPago
from sqlalchemy import Column, ForeignKey

import uuid

Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contratos"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4)
    tipoContrato = db.Column(db.String)
    fechaInicio = db.Column(db.DateTime)
    fechaTerminacion = db.Column(db.DateTime)
    pago = db.relationship('Pago')
    informacionCatastral = db.Column(db.String) # ID

class Pago(db.Model):
    __tablename__ = "pagos"
    contratoId = Column(db.String, ForeignKey("contratos.id"), primary_key=True)
    valorPago = db.Column(db.Float)
    tipoMoneda = db.Column(db.String)
    metodoPago = db.Column(db.String)
