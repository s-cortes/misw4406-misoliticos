from propiedades.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

#Tablas intermedias
#poligonos_coordenadas = db.Table(
#    "poligonos_coordenadas",
#    db.Model.metadata,)


#Tablas objetos de valor
class Direccion(db.Model):
    __tablename__ = "direccion"
    valor = db.Column(db.String(100), primary_key=True, nullable=False)

class Coordenada(db.Model):
    __tablename__ = "coordenada"
    latitude = db.Column(db.Float, primary_key=True, nullable=False)
    longitud = db.Column(db.Float, primary_key=True, nullable=False)

class Poligono(db.Model):
    __tablename__ = "poligono"
    coordenada = db.relationship('Coordenada', backref='poligono')

#Tablas de entidades

class Lote(db.Model):
    __tablename__ = "lote"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4, nullable=False)
    direccion = db.relationship('Direccion', backref='lote')
    poligono = db.relationship('Poligono', backref='lote')
    edificio = db.relationship('Edificio', backref='lote')

class Edificio(db.Model):
    __tablename__ = "edificio"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4, nullable=False)
    poligono = db.relationship('Poligono', backref='edificio')




