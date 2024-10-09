from consoleTextStyle import ConsoleTextStyle as CoTeSt


def personal_sum(_numbers) -> tuple:
    incorrect_data = result = 0
    for number in _numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            continue
    return result, incorrect_data


def calculate_average(_numbers):
    try:
        result = personal_sum(_numbers)
        if result[1] != 0:
            raise TypeError
        return result[0]/len(_numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        CoTeSt.colorful_text("В numbers записан некорректный тип данных", CoTeSt.Color.RED)
        return None


if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
    print(f'Результат 5: {calculate_average([])}')  # Должен вывестись ноль
