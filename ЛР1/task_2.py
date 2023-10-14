# TODO Найдите количество книг, которое можно разместить на дискете

# Объем дискеты в байтах
capacity_diskette = 1.44 * 1024 * 1024

# Количество страниц в книге
page = 100

# Число строк на странице
Number_of_rows = 50

# Количество символов в строке
characters_per_line = 25

# Размер одной книги в байтах
book_size = page * Number_of_rows  * characters_per_line * 4

# Число книг которе можно поместить на дискету
books_on_diskette = int(capacity_diskette // book_size)


print("Количество книг, помещающихся на дискету:", books_on_diskette)
