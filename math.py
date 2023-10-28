def add(number1: int, number2: int) -> int:
    return number1 + number2

def substraction(number1: int, number2: int) -> int:
    if number1 > number2:
        return number1 - number2
    else:
        return number2 - number1

def multiplication(number1: int, number2: int) -> int:
    return number1 * number2

def division(number1: int, number2: int) -> int:
    if number2 == 0:
        raise ZeroDivisionError
    return number1 // number2
