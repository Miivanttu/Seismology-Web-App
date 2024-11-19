from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'seismika'

    from .views import views
    from .auth import auth
    from .calc import calc
    from .graph import graph

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(calc, url_prefix='/')
    app.register_blueprint(graph, url_prefix='/')

    return app