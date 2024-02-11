if __name__ == "__main__":
    # Write your solution here
    class Machine:
        """
        Base class representing a machine.
        """

        def __init__(self, name: str, manufacturer: str, year: int):
            """
            Initialize the machine.

            :param name: The name of the machine.
            :param manufacturer: The manufacturer of the machine.
            :param year: The year of manufacture of the machine.
            """
            self.name = name
            self.manufacturer = manufacturer
            self.year = year

        def start(self) -> str:
            """
            Start the machine.

            :return: A message indicating the machine has started.
            """
            return f"{self.name} from {self.manufacturer} has started."

        def stop(self) -> str:
            """
            Stop the machine.

            :return: A message indicating the machine has stopped.
            """
            return f"{self.name} from {self.manufacturer} has stopped."

        def __str__(self) -> str:
            """
            Return a string representation of the machine.

            :return: A string with the name, manufacturer, and year of the machine.
            """
            return f"{self.name} ({self.manufacturer}, {self.year})"

        def __repr__(self) -> str:
            """
            Return a string representation of the machine for eval or repr.

            :return: A string with the class name and attributes.
            """
            return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r}, year={self.year!r})"


    class Lathe(Machine):
        """
        Child class representing a lathe, inheriting from Machine.
        """

        def __init__(self, name: str, manufacturer: str, year: int, max_speed: float):
            """
            Initialize the lathe.

            :param name: The name of the lathe.
            :param manufacturer: The manufacturer of the lathe.
            :param year: The year of manufacture of the lathe.
            :param max_speed: The maximum speed of the lathe.
            """
            super().__init__(name, manufacturer, year)
            self.max_speed = max_speed

        def start(self) -> str:
            """
            Start the lathe with a special message.

            :return: A message indicating the lathe has started.
            """
            return f"{self.name} from {self.manufacturer} with max speed {self.max_speed} RPM has started."

        def change_speed(self, new_speed: float) -> str:
            """
            Change the speed of the lathe.

            :param new_speed: The new speed to set for the lathe.
            :return: A message indicating the lathe speed has been changed.
            """
            return f"{self.name} speed has been changed to {new_speed} RPM."

        def __str__(self) -> str:
            """
            Return a string representation of the lathe.

            :return: A string with the name, manufacturer, year, and max speed of the lathe.
            """
            return f"{super().__str__()} - Lathe, Max speed: {self.max_speed} RPM"

        def __repr__(self) -> str:
            """
            Return a string representation of the lathe for eval or repr.

            :return: A string with the class name and attributes.
            """
            return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r}, year={self.year!r}, max_speed={self.max_speed!r})"

    pass
