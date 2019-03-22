import os
from flask import Flask, render_template
from flaskr import db


#
def page_not_found(e):
    return render_template('nope.html'), 404


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_error_handler(404, page_not_found)
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
    return render_template('index.html')

@app.route('/first_puzzle')
def first_puzzle():
    cur = db.get_db().cursor()
    return render_template('first_puzzle.html')


@app.route('/themetagames')
@app.route('/themetagame')
@app.route('/metagame')
@app.route('/metagames')
def second_puzzle():
    return render_template('second_puzzle.html')


@app.route('/july+16')
def third_puzzle():
    return render_template('third_puzzle.html')

@app.route('/014251')
def fourth_puzzle():
    return render_template('fourth_puzzle.html')

@app.route('/006')
def fifth_puzzle():
    return render_template('fifth_puzzle.html')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host= '0.0.0.0') # to run on computers public ip
