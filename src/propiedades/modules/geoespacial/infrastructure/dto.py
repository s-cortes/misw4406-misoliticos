from propiedades.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = db.declarative_base()

class Lote(db.Model):
    __tablename__ = "lote"
    id = db.Column(db.String, primary_key=True)
    direcciones = db.Column(db.String, nullable=False)
    coordenadas_poligono = db.Column(db.String, nullable=False)
    edificio = db.relationship('Edificio', backref='edificio')

class Edificio(db.Model):
    __tablename__ = "edificio"
    id = db.Column(db.String, primary_key=True)
    coordenadas_poligono = db.Column(db.String)
    lote_id = db.Column(db.String, db.ForeignKey("lote.id"))

