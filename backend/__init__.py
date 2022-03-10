import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def registerBlueprints(app):
    from backend.main import mainBlueprint
    from backend.api import apiBlueprint

    app.register_blueprint(apiBlueprint)
    app.register_blueprint(mainBlueprint)



def create_app(configClass='DevConfig'):
    # create and configure the app
    app = Flask(
        __name__, 
        instance_relative_config=False,
        static_folder="../frontend/build",
        static_url_path="/"
    )

    app.config.from_object("config.DevConfig")

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    db.init_app(app)
    with app.app_context():
        registerBlueprints(app)
        db.create_all()
    
    return app

