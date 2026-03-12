def check_number(num):

    if num.isdigit():
        number = int(num)
        return number

    else:
        raise ValueError('Ошибка: Вводимое значение должно содержать только цифры')
