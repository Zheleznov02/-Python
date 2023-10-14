users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

# Пустой словарь для статистики
dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

# Общее количество
dictionary["Общее количество"] = len(users)

# Уникальные посещения р
unique_visitors = set(users)
dictionary["Уникальные посещения"] = len(unique_visitors)

# Выводим словарь статистики
print(dictionary)