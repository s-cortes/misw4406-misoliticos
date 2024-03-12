from sqlalchemy import Boolean, Column, ForeignKey, Integer, Table, func
from sqlalchemy.orm import declarative_base, relationship

from propiedades.config.db import db

Base = db.declarative_base()


class Saga(db.Model):
    __tablename__ = "sagas"
    id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.Integer, primary_key=True)
    is_last = db.Column(db.Boolean, nullable=False, default=False)
    event = db.Column(db.String, nullable=False, default='')
    error = db.Column(db.String, nullable=False, default='')
    command = db.Column(db.String, nullable=False, default='')
    compensation = db.Column(db.String, nullable=False, default='')
    topic = db.Column(db.String, nullable=False, default='')


class Transaction(db.Model):
    __tablename__ = "transactiones"
    id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.Integer, primary_key=True)
    correlation_id = db.Column(db.String, primary_key=True)

    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())
    status = db.Column(db.String, nullable=False, default='')
