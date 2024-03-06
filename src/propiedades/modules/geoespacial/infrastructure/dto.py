from propiedades.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Lote(db.Model):
    __tablename__ = "lote"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4, nullable=False)
    direcciones = db.Column(db.String(400))
    coordenadas_poligono = db.Column(db.String(400))
    edificio = db.relationship('Edificio', backref='edificio')

class Edificio(db.Model):
    __tablename__ = "edificio"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4, nullable=False)
    coordenadas_poligono = db.Column(db.String(400))
    lote_id = db.Column(db.String, db.ForeignKey("lote.id"))

