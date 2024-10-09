from consoleTextStyle import ConsoleTextStyle as CoTeSt


class Car:
    def __new__(cls, model, vin, numbers):
        try:
            cls.__is_vin_valid(vin)
            cls.__is_numbers_valid(numbers)
            return super().__new__(cls)
        except Car.IncorrectVinNumber as exc:
            CoTeSt.colorful_text(exc.message, CoTeSt.Color.RED)
        except Car.IncorrectCarNumbers as exc:
            CoTeSt.colorful_text(exc.message, CoTeSt.Color.RED)

    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        print(f"{self.model} успешно создан")

    @staticmethod
    def __is_vin_valid(vin_number):
        if not isinstance(vin_number, int):
            raise Car.IncorrectVinNumber("Некорректный тип vin номера")
        elif not 1_000_000 <= vin_number <= 9_999_999:
            raise Car.IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    @staticmethod
    def __is_numbers_valid(_numbers) -> bool:
        if not isinstance(_numbers, str):
            raise Car.IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(_numbers) != 6:
            raise Car.IncorrectVinNumber("Неверная длина номера")
        else:
            return True

    class IncorrectVinNumber(Exception):
        def __init__(self, message):
            self.message = message

    class IncorrectCarNumbers(Exception):
        def __init__(self, message):
            self.message = message


if __name__ == "__main__":
    first = Car('Model1', 1000000, 'f123dj')
    second = Car('Model2', 300, 'т001тр')
    third = Car('Model3', 2020202, 'нет номера')
