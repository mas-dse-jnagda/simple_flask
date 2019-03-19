import os
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    import db
    db.init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first_puzzle')
def first_puzzle():
    #http://flask.pocoo.org/docs/1.0/patterns/sqlite3/
    return render_template('puzzle.html')


if __name__ == '__main__':
    app.run(debug=True)
