import calendar
import datetime
import re


def parse_text_for_expenses(text):
    """Парсит по тексту. Ищет: Продукты 2000"""
    reg = re.match(r'^([А-Яа-яa-zA-Z]+)([ ]?[-|=|_]?[ ]?)([\d]+[.,]?[\d]*)$', text)
    if not reg or not reg.group(3):
        return False
    return reg.group(1), float(reg.group(3))


def get_one_day_data_for_db(year: int, month: int, day: int):
    """Получить полный день"""
    start = datetime.date(year=year, month=month, day=day)
    end = datetime.datetime(year=year, month=month, day=day, hour=23, minute=59, second=59)
    return start, end


def get_one_nedel9_data_for_db(year: int, month: int, day: int):
    """Получить 1 неделю"""
    day_end = datetime.date(year=year, month=month, day=day)
    ls = datetime.timedelta(days=7)
    start = day_end - ls
    return start, day_end


def get_month_data_for_db(year: int, month: int):
    """Получить 1 месяц"""
    start = datetime.date(year=year, month=month, day=1)
    last_day = calendar.monthrange(year, month)[1]
    end = datetime.datetime(year=year, month=month, day=last_day, hour=23, minute=59, second=59)
    return start, end


def get_year_data_for_db(year: int):
    """Получить 1 год"""
    start = datetime.date(year=year, month=1, day=1)
    end = datetime.datetime(year=year, month=12, day=31, hour=23, minute=59, second=59)
    return start, end
