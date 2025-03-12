import os

from flask import Flask


def create_app(test_config=None):
    # create config app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'recipes.sqlite'),
    )

    if test_config is None:
        # load instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'hey world'

    # register db commands
    from . import db
    db.init_app(app)

    return app