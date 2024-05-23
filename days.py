from datetime import datetime


class Days:
    def days_of_period(self):
        start_day = int(input('начальный день'))
        start_month = int(input('начальный месяц'))
        start_year = int(input('начальный год'))
        end_day = int(input('конечный день'))
        end_month = int(input('конечный месяц'))
        end_year = int(input('конечный год'))
        start_date = datetime(start_year, start_month, start_day)
        end_date = datetime(end_year, end_month, end_day)
        period_days = (end_date - start_date).days
        return period_days, end_date


days = Days()
period_days, end_date = days.days_of_period()
