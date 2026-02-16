
def add(x, y):
    print(type(x))
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Ошибка!!!! Нужно ввести число")
    
    return x+y
# try:
    
#     print(add(8, '6'))
# except TypeError as e:
#     print(e)