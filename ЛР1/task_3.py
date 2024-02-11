list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

# Общее количество игроков
players = len(list_players)

# Разделяем игроков на две команды

team1 = list_players[1::2]
team2=  list_players[::2]

# Игроки в каждой команде
print(team2)
print(team1)
