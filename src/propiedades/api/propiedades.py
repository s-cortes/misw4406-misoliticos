from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger
from flask_sqlalchemy import SQLAlchemy


def register_handlers():
    import propiedades.modules.propiedades.application


def import_alchemy_models():
    import propiedades.modules.propiedades.infrastructure.dtos


def consume():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    from propiedades.modules.propiedades.infrastructure.consumers import (
        subscribe_to_events,
        subscribe_to_commands,
    )

    # Suscripción a eventos
    threading.Thread(target=subscribe_to_events).start()

    # Suscripción a comandos
    threading.Thread(target=subscribe_to_commands).start()


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
            consume()

    # Importa Blueprints
    from propiedades.modules.propiedades.presentation.api import bp

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
