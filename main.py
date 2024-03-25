from _pydatetime import datetime

def many_of_day():
    many_day = int(input())
    return many_day

def many_of_period():
    period_many = many_of_day() * days_of_period()


def days_of_period():
    start_day = int(input('начальный день'))
    start_month = int(input('начальный месяц'))
    start_year = int(input('начальный год'))
    end_day = int(input('конечный день'))
    end_month = int(input('конечный месяц'))
    end_year = int(input('конечный год'))
    start_date = datetime(start_year, start_month, start_day)
    end_date = datetime(end_year, end_month, end_day)
    period_days = (end_date - start_date).days

    return period_days

def remains():
    pass

def ait_remains():
    pass

def itog():
    pass