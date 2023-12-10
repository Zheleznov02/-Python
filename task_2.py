import doctest


class SeaCruiser:
    def __init__(self, max_speed: float, current_speed: float, is_engine_on: bool):
        """
        Создание и подготовка к работе объекта "Морской катер"

        :param max_speed: Максимальная скорость катера
        :param current_speed: Текущая скорость катера
        :param is_engine_on: Состояние двигателя (включен или выключен)

        Примеры:
        >>> cruiser = SeaCruiser(50, 0, False)  # инициализация экземпляра класса
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed

        if not isinstance(current_speed, (int, float)):
            raise TypeError("Текущая скорость должна быть int или float")
        if current_speed < 0:
            raise ValueError("Текущая скорость не может быть отрицательным числом")
        self.current_speed = current_speed

        if not isinstance(is_engine_on, bool):
            raise TypeError("Состояние двигателя должно быть булевым значением")
        self.is_engine_on = is_engine_on

    def start_engine(self) -> None:
        """
        Метод запуска двигателя морского катера.

        Примеры:
        >>> cruiser = SeaCruiser(50, 0, False)
        >>> cruiser.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Метод остановки двигателя морского катера.

        Примеры:
        >>> cruiser = SeaCruiser(50, 20, True)
        >>> cruiser.stop_engine()
        """
        ...

    def increase_speed(self, speed_increase: float) -> None:
        """
        Метод увеличения скорости морского катера.

        :param speed_increase: Значение, на которое увеличивается скорость

        :raise ValueError: Если увеличение скорости приведет к превышению максимальной скорости,
        то вызывается ошибка

        Примеры:
        >>> cruiser = SeaCruiser(50, 30, True)
        >>> cruiser.increase_speed(10)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
