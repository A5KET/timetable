import flask


app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/<timetable>')
def timetable(timetable): 
    return f'<h1>Your timetable {timetable}'