from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first_puzzle')
def first_puzzle():
    return render_template('puzzle.html')


if __name__ == '__main__':
    app.run(debug=True)
