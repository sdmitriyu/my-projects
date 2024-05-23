class Many_of_day:
    def __init__(self, many_day):
        self.many_day = many_day

    def return_many_day(self):
        return self.many_day


manyDay = Many_of_day(float(input('Какую сумму в день вы планируете тратить ')))

retManyDay = manyDay.return_many_day()
