# Импортируем ваши фичи из папки src
from src.calculator import add
from src.cli_cnt_files import count_files

def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить калькулятор")
    print("2. Запустить счетчик файлов")
    
    choice = input("Введите номер: ")
    
    if choice == "1":
        print('----Запущен режим калькулятора----')
        try:
            value1 = input('Введите первое число: ')
            value2 = input('Введите второе число: ')
            result = add(int(value1), int(value2))
            print(f'Результат сложения равен: {result}')
        except ValueError as e:
            e = 'Вводить нужно только целые числа'
            print(e)
            
    elif choice == "2":
        count_files()
    else:
        print("Ошибка: такого варианта нет. Попробуйте снова!")

# Магическая проверка: запущен ли файл напрямую
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма принудительно завершена пользователем.")
    except Exception as e:
        print(f"Упс! Произошла непредвиденная ошибка: {e}")