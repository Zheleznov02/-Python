import doctest


class RocketLauncher:
    def __init__(self, max_rocket_capacity: int, current_rocket_count: int, is_launcher_ready: bool):
        """
        Создание и подготовка к работе объекта "Ракетная шахта"

        :param max_rocket_capacity: Максимальная вместимость ракетной шахты
        :param current_rocket_count: Текущее количество ракет в шахте
        :param is_launcher_ready: Готовность ракетной шахты к запуску

        Примеры:
        >>> launcher = RocketLauncher(10, 0, False)  # инициализация экземпляра класса
        """
        if not isinstance(max_rocket_capacity, int):
            raise TypeError("Максимальная вместимость должна быть целым числом")
        if max_rocket_capacity <= 0:
            raise ValueError("Максимальная вместимость должна быть положительным числом")
        self.max_rocket_capacity = max_rocket_capacity

        if not isinstance(current_rocket_count, int):
            raise TypeError("Текущее количество ракет должно быть целым числом")
        if current_rocket_count < 0:
            raise ValueError("Текущее количество ракет не может быть отрицательным числом")
        self.current_rocket_count = current_rocket_count

        if not isinstance(is_launcher_ready, bool):
            raise TypeError("Готовность ракетной шахты должна быть булевым значением")
        self.is_launcher_ready = is_launcher_ready

    def load_rocket(self, count: int) -> None:
        """
        Метод загрузки ракет в ракетную шахту.

        :param count: Количество загружаемых ракет

        :raise ValueError: Если количество загружаемых ракет превышает свободное место в шахте, то вызывается ошибка

        Примеры:
        >>> launcher = RocketLauncher(10, 0, False)
        >>> launcher.load_rocket(5)
        """
        ...

    def launch_rocket(self, count: int) -> None:
        """
        Метод запуска ракет из ракетной шахты.

        :param count: Количество запускаемых ракет

        :raise ValueError: Если количество запускаемых ракет превышает количество ракет в шахте,
        то вызывается ошибка

        Примеры:
        >>> launcher = RocketLauncher(10, 5, True)
        >>> launcher.launch_rocket(3)
        """
        ...

    def prepare_for_launch(self) -> None:
        """
        Метод подготовки ракетной шахты к запуску.

        Примеры:
        >>> launcher = RocketLauncher(10, 5, False)
        >>> launcher.prepare_for_launch()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
