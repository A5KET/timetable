import flask

from . import main


@main.route('/')
def index():
    return flask.render_template('index.html')

@main.route('/timetable/find_timetable', methods=['GET'])
def find_table():
    table_id = flask.request.args.get('id')
    if table_id:
        return flask.redirect('/table/' + table_id)

@main.route('/timetable/new_timetable', methods=['GET', 'POST'])
def create_table():
    return flask.render_template('/timetable/create_table.html')
    


@main.route('/timetable/<timetable_name>')
def timetable(timetable_name):
    return flask.render_template('timetable/timetable.html',
                                timetable_name=timetable_name,
                                days_of_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )

