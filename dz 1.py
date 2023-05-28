def day_of_week(number):
    week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if 1 <= number <= 7:
        return week_days[number-1]
    else:
        return "Неверно, пожалуйста, введите число от 1 до 7"

number = 0
while not (1 <= number <= 7):
    user_input = input("Введите номер дня недели (от 1 до 7): ")
    number = int(user_input)
    if not (1 <= number <= 7):
        print("Неверно, пожалуйста, введите число от 1 до 7")
print(day_of_week(number))
