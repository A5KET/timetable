import flask


app = flask.Flask(__name__)

@app.route('/<name>')
def index(name):
    return flask.render_template("index.html", name=name)