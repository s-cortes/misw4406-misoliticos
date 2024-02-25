from propiedades.config.db import db
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
    oficinas = db.relationship('Oficina')

class Oficina(db.Model):
    __tablename__ = "oficinas"
    nombre = db.Column(db.String, primary_key=True)
    division = db.Column(db.String)
    telefono = db.Column(db.String)
    unidadArea = db.Column(db.String)
    valorArea = db.Column(db.Float)
    