from propiedades.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Lote(db.Model):
    __tablename__ = "lote"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4)
#    direccion = 
#    poligono =
    edificio = db.relationship('Edificio')

class Direccion(db.Model):
    __tablename__ = "direccion"
    LoteId = Column(db.String, ForeignKey("lote.id"), primary_key=True)
    valor = db.Column(db.String)

#class Poligono(db.Model):
#    __tablename__ = "poligono"

class Edificio(db.Model):
    __tablename__ = "edificio"
    id = Column(db.String, primary_key=True, default=uuid.uuid4)
    Loteid = Column(db.String, ForeignKey("lote.id"))
