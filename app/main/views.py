import flask

from . import main


@main.route('/')
def index():
    return flask.render_template('index.html')


@main.route('/<timetable_name>')
def timetable(timetable_name):
    return flask.render_template('timetable.html',
                                timetable_name=timetable_name,
                                days_of_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )