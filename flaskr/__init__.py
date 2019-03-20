import os
from flask import Flask, render_template
from flaskr import db


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
    db.init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
    cur = db.get_db().cursor()
    return render_template('index.html')


@app.route('/first_puzzle')
def first_puzzle():
    cur = db.get_db().cursor()
    return render_template('first_puzzle.html')


@app.route('/themetagames')
@app.route('/themetagame')
def second_puzzle():
    return render_template('second_puzzle.html')


@app.route('/may+15')
@app.route('/may+16')
@app.route('/may+19')
@app.route('/june+17')
@app.route('/june+18')
@app.route('/july+14')
@app.route('/aug+14')
@app.route('/aug+15')
@app.route('/aug+17')
def wrong_date():
    return render_template('nope.html')


@app.route('/july+16')
def third_puzzle():
    return render_template('third_puzzle.html')


if __name__ == '__main__':
    app.run(debug=True)
