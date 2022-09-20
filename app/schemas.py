from . import marshmallow as ma
from .models import Timetable, Week, Day, Event


class EventSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Event

    name = ma.auto_field()
    description = ma.auto_field()
    person = ma.auto_field()
    start_time = ma.auto_field()
    end_time = ma.auto_field()


class DaySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Day

    weekday = ma.Method('get_weekday')
    events = ma.List(ma.Nested(EventSchema))

    def get_weekday(self, obj: Day):
        return obj.weekday.value



class WeekSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Week

    week_number = ma.auto_field()
    days = ma.List(ma.Nested(DaySchema))


class TimetableSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Timetable

    name = ma.auto_field()
    weeks = ma.List(ma.Nested(WeekSchema))

