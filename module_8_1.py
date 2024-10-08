from decimal import Decimal, InvalidOperation


def add_everything_up(first_addendum, second_addendum):
    try:  # Код ниже нужен для решения проблемы сложения двух float
        return float(Decimal(first_addendum).quantize(Decimal(str(first_addendum))) +
                     Decimal(second_addendum).quantize(Decimal(str(second_addendum))))
    except InvalidOperation:
        return str(first_addendum) + str(second_addendum)


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, "7"))
    print(add_everything_up(123.456, 7))
    print(add_everything_up(5, 7))
