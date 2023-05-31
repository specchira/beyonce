def get_drink(profession):
    MENU = {
        "Студент": "Текила Patron",
        "Завуч": "Ерш",
        "Программист": "Хипстерское крафтовое пиво",
        "Байкер": "Самогон",
        "Чиновник": "Ваши налоги",
        "Рэпер": "Кристалл",
        "Прочие": "Пиво"
    }
    return MENU.get(profession.capitalize(), 'Пиво')
profession = input('Введи профессию: ')    
print(get_drink(profession))