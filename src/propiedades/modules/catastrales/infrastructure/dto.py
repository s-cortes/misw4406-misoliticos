from config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Inmueble(db.Model):
    __tablename__ = "inmuebles"
    id = db.Column(db.String, primary_key=True)
    fechaCreacion = db.Column(db.DateTime)
    pisos = db.relationship('Piso')

class Piso(db.Model):
    __tablename__ = "pisos"
    inmuebleId = Column(db.String, ForeignKey("inmuebles.id"), primary_key=True)
    oficinas = db.relationship('Oficina')

class Oficina(db.Model):
    __tablename__ = "oficinas"
    PisoId = Column(db.String, ForeignKey("pisos.inmuebleId"), primary_key=True)
    nombre = db.Column(db.String, primary_key=True)
    division = db.Column(db.String)
    telefono = db.Column(db.String)
    unidadArea = db.Column(db.String)
    valorArea = db.Column(db.Float)
    