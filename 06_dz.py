dictionary_of_numbers = { "0": "ноль", "1":"один", "2": "два", "3":"три", "4":"четыре", "5": "пять", "6": "шесть", "7": "семь", "8":"восемь", "9":"девять", "10000": "нет"}
number_key = input("введите число ")
try:
    print(dictionary_of_numbers[number_key])
except KeyError: 
    print("такого номера нет")
