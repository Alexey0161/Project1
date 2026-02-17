# Импортируем ваши фичи из папки src
from src.calculator import add
from src.filesystem.cli_cnt_files import count_files
from src.filesystem.cli_modif_files_2 import process_logic

def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить калькулятор")
    print("2. Запустить счетчик файлов")
    print("3. Запустить установщик даты в имя файла")
    
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
        print('----Запуcкает счетчик файлов в папке----')
        try:
            target_dir = input('Введите полный путь к папке: ').strip().replace('"', '')
            count_files(target_dir)
        except Exception as e:
            
            print(e)

    elif choice == "3":
        print('----Запускает установщик даты в имена файлов ----')
        target_dir = input('Введите полный путь к папке: ').strip().replace('"', '')
        print('1. Запускает установку даты в имена во всех папках, в том числе и ВЛОЖЕННЫХ')
        print('2. Запускает установку даты в именах всех файлов ТОЛЬКО в выбранной папке')
        sub_choice = input('Введите номер: ')
        try:
            if sub_choice == '1':
                process_logic(target_dir, True)
            elif sub_choice == '2':
                process_logic(target_dir)
            elif sub_choice == '':
                print('Пустой ввод. Программа прервана. Повторите ввод заново')
            else:
                print('Ошибка ввода. Повторите ввод заново. Выполняется выход из программы')
                return
        except Exception as e:
            
            print(e)
        
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
                