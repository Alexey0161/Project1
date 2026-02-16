def add(x, y):
    # Логика не должна гадать, числа это или нет. 
    # Если мы здесь, значит main.py уже всё проверил.
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Внутренняя ошибка: add ожидает числа")
    return x + y