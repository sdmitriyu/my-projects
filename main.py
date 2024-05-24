from days import Days
from many_day import Many_of_day

# Создаем экземпляры классов
days_instance = Days()

money_per_day = input('Сколько денег в день вы планируете потратить? ')
try:
    money_per_day = float(money_per_day)  # Преобразуем ввод пользователя в число
except ValueError:
    print("Пожалуйста, введите число")

many_day = Many_of_day(money_per_day)

# Получаем результаты от методов классов
days_period_days, end_date = days_instance.days_of_period()
many_day_result = many_day.return_many_day()

# Вычисляем итоговый результат
result = days_period_days * many_day_result
print(result)