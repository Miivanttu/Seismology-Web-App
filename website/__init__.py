from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'afsD^&Wdg77a6wduAIwdyugy23by3hseyury3i278*AYwdawyuq8&&*&YDW*&Dwu'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .calc import calc
    from .graph import graph
    from .andmed import andmed

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(calc, url_prefix='/')
    app.register_blueprint(graph, url_prefix='/')
    app.register_blueprint(andmed, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app