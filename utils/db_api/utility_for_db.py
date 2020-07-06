import calendar
import datetime


def get_one_day_data_for_db(year, month, day):
    start = datetime.date(year=year, month=month, day=day)
    end = datetime.datetime(year=year, month=month, day=day, hour=23, minute=59, second=59)
    return start, end


def get_one_nedel9_data_for_db(year, month, day):
    start = datetime.date(year=year, month=month, day=day)
    ls = datetime.timedelta(days=7)
    end = start - ls
    return start, end





def get_month_data_for_db(year, month):
    start = datetime.date(year=year, month=month, day=1)
    last_day = calendar.monthrange(year, month)[1]
    end = datetime.datetime(year=year, month=month, day=last_day, hour=23, minute=59, second=59)
    return start, end


def get_year_data_for_db(year):
    start = datetime.date(year=year, month=1, day=1)
    end = datetime.datetime(year=year, month=12, day=31, hour=23, minute=59, second=59)
    return start, end
