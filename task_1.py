import doctest


class Submarine:
    def __init__(self, max_depth: float, current_depth: float):
        """
        Создание и подготовка к работе объекта "Подводный необитаемый аппарат"

        :param max_depth: Максимальная глубина погружения аппарата
        :param current_depth: Текущая глубина погружения аппарата

        Примеры:
        >>> submarine = Submarine(1000, 0)  # инициализация экземпляра класса
        """
        if not isinstance(max_depth, (int, float)):
            raise TypeError("Максимальная глубина должна быть типа int или float")
        if max_depth <= 0:
            raise ValueError("Максимальная глубина должна быть положительным числом")
        self.max_depth = max_depth

        if not isinstance(current_depth, (int, float)):
            raise TypeError("Текущая глубина должна быть типа int или float")
        if current_depth < 0:
            raise ValueError("Текущая глубина не может быть отрицательным числом")
        if current_depth > max_depth:
            raise ValueError("Текущая глубина не может превышать максимальную глубину")
        self.current_depth = current_depth

    def dive(self, depth: float) -> None:
        """
        Погружение аппарата на заданную глубину.

        :param depth: Глубина погружения
        :raise ValueError: Если глубина погружения превышает максимальную глубину аппарата,
        то вызывается ошибка.

        Примеры:
        >>> submarine = Submarine(1000, 0)
        >>> submarine.dive(500)
        """
        ...

    def emerge(self, depth: float) -> None:
        """
        Всплытие аппарата на заданную глубину.

        :param depth: Глубина всплытия
        :raise ValueError: Если глубина всплытия превышает текущую глубину аппарата,
        то вызывается ошибка.

        Примеры:
        >>> submarine = Submarine(1000, 500)
        >>> submarine.emerge(200)
        """
        ...

    def status(self) -> str:
        """
        Получение статуса аппарата (глубина погружения).

        :return: Текущая глубина погружения.

        Примеры:
        >>> submarine = Submarine(1000, 800)
        >>> submarine.status()
        'Текущая глубина: 800 м'
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
