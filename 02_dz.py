x = input('Введи профессию: ')
MENU = {
    "Студент": "Текила Patron",
    "Завуч": "Ерш",
    "Программист": "Хипстерское крафтовое пиво",
    "Байкер": "Самогон",
    "Чиновник": "Ваши налоги",
    "Рэпер": "Кристалл",
    "Прочие": "Пиво"
}
print(MENU.get(x.capitalize(),'Пиво'))