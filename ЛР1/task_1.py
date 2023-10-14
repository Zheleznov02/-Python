numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_missing_item = 4

# Найдем сумму всех элементов, кроме пропуска (None)
sum_of_numbers = sum(numbers[:index_missing_item]) + sum(numbers[index_missing_item+1:])

# Найдем количество элементов, включая пропуск
count_of_numbers = len(numbers)

# Вычислим среднее арифметическое всех остальных элементов
average = sum_of_numbers / count_of_numbers

# Заменим пропущенный элемент средним арифметическим
numbers[index_missing_item] = average

# Выведем обновленный список
print("Измененный список:", numbers)
