from datetime import datetime

class Expenses:
    def __init__(self, expenses):
        self.expenses = expenses
        self.daynow = datetime.date()
    def ret(self):
        return self.expenses(int(input()))

    def