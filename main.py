# Импортируем ваши фичи из папки src
from src.calculator import add
from src.filesystem.cli_cnt_files import count_files

def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить калькулятор")
    print("2. Запустить счетчик файлов")
    
    choice = input("Введите номер: ")
    
 
    if choice == "1":
        try:
            # Валидация происходит ЗДЕСЬ
            v1 = float(input('Введите x: ')) 
            v2 = float(input('Введите y: '))
            
            # Передаем уже ЧИСТЫЕ данные в логику
            print(f"Результат: {add(v1, v2)}")
            
        except ValueError:
            print("Критическая ошибка: Вы ввели не число! Попробуйте еще раз.")
            
    elif choice == "2":
        print('----Запущет счетчик файлов в папке----')
        try:
            target_dir = input('Введите полный путь к папке: ')
            count_files(target_dir)
        except Exception:
            print('Такого пути не существует')
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
                