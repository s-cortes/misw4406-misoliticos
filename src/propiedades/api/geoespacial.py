from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger
from flask_sqlalchemy import SQLAlchemy


def register_handlers():
    import propiedades.modules.geoespacial.application


def import_alchemy_models():
    import propiedades.modules.geoespacial.infrastructure.dto


def consume(app):
    import threading
    from propiedades.modules.geoespacial.infrastructure.consumers import (
        subscribe_to_events,
        subscribe_to_commands,
    )

    # Suscripción a eventos
    threading.Thread(target=subscribe_to_events).start()

    # Suscripción a comandos
    threading.Thread(target=subscribe_to_commands, args=[app]).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    from propiedades.config.db import generate_database_uri

    app.config["SQLALCHEMY_DATABASE_URI"] = generate_database_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.secret_key = "9d58f98f-3ae8-4149-a09f-3a8c2012e32c"
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["TESTING"] = configuracion.get("TESTING")

    # Inicializa la DB
    from propiedades.config.db import init_db

    init_db(app)

    from propiedades.config.db import db

    import_alchemy_models()
    register_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            consume(app)

    # Importa Blueprints
    from propiedades.modules.geoespacial.presentation.api import bp

    # Registro de Blueprints
    app.register_blueprint(bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag["info"]["version"] = "1.0"
        swag["info"]["title"] = "Propiedades de los Alpes API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "healthy"}

    return app