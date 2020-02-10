import os

from flask import Flask

from flaskr.infrastructure.database import db
from flaskr.application import auth
from flaskr import blog


def create_app(test_config=None):
    # create and configure the app
    building_app = Flask(__name__, instance_relative_config=True)
    building_app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(building_app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        building_app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        building_app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(building_app.instance_path)
    except OSError:
        pass

    db.init_app(building_app)

    building_app.register_blueprint(auth.bp)

    building_app.register_blueprint(blog.bp)
    building_app.add_url_rule('/', endpoint='index')

    return building_app


app = create_app()
