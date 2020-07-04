import calendar
import datetime


def get_data_for_db(year, month):
    start = datetime.date(year=year, month=month, day=1)
    last_day = calendar.monthrange(year, month)[1]
    end = datetime.date(year=year, month=month, day=last_day)
    return start, end


