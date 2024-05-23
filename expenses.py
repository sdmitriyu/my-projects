class Expenses:
    def __init__(self, expenses):
        self.expenses = expenses

    def ret(self):
        return self.expenses(int(input()))
