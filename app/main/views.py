import flask

from . import main


@main.route('/')
def index():
    return flask.render_template('index.html')


@main.route('/table/<table_name>')
def timetable(table_name):
    return flask.render_template('timetable.html',
                                timetable_name=table_name,
                                days_of_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )
