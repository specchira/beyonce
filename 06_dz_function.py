def get_number(dictionary_of_numbers):
    number_key = input("введите число ")
    try:
        return dictionary_of_numbers[number_key]
    except KeyError:
        return "такого номера нет"
    
dictionary_of_numbers = { "0": "ноль", "1":"один", "2": "два", "3":"три", "4":"четыре", "5": "пять", "6": "шесть", "7": "семь", "8":"восемь", "9":"девять", "10000": "нет"}
print(get_number(dictionary_of_numbers))