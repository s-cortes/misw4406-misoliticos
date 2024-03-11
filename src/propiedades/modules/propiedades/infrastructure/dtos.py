from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

from propiedades.config.db import db

Base = db.declarative_base()


class Fotografia(db.Model):
    __tablename__ = "fotografias"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)

    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)

    valor_contenido = db.Column(db.String, nullable=False)
    tipo_contenido = db.Column(db.String, nullable=False)

    propiedad_id = db.Column(db.String, db.ForeignKey("propiedades.id"))


class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)

    tipo_construccion = db.Column(db.String, nullable=False)
    entidad = db.Column(db.String, nullable=False)

    fotografias = db.relationship("Fotografia", backref="fotografias")
