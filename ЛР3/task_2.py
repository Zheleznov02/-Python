# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    # Разделяем строки на списки имен с использованием заданного разделителя
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Преобразуем списки имен в множества для нахождения общих участников
    set1 = set(participants1)
    set2 = set(participants2)
    common_participants = set1.intersection(set2)

    # Возвращаем список общих участников, отсортированный в алфавитном порядке
    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group)

print("Общие участники групп (отсортированные):",common_participants)
