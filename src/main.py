# Импортируем ваши фичи из папки src
from src.calculator import add
from src.filesystem.cli_cnt_files import count_files
from src.filesystem.cli_modif_files_2 import process_logic
from src.filesystem.cli_find_file import find_file
from src.filesystem.cli_copy_files import copy_file

# импортируем модуль логирования
import logging


def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить копировальщик файлов")
    print("2. Запустить счетчик файлов")
    print("3. Запустить поисковик файлов")
    print("4. Запустить установщик даты в имя файла")
    print("11. Запустить калькулятор")
    
    
    
    
    choice = input("Введите номер: ")
    if choice == "1":
        print('----Запускает копировальщик файлов ----')
        try:
            filename = input('Введите имя файла, который надо скопировать: ')
            copy_file(filename)
        except Exception as e:
                
                print(e)
        

    elif choice == "2":
        print('----Запуcкает счетчик файлов в папке----')
        try:
            target_dir = input('Введите полный путь к папке: ').strip().replace('"', '')
            count_files(target_dir)
        except Exception as e:
            
            print(e)
    elif choice == "3":
        print('----Запускает поисковик файлов по фильтру: размер меньше заданного значения-----')
        target_dir = input('Введите полный путь к папке: ').strip().replace('"', '')
        size = input('Введите размер, меньше которого должны быть найденные файлы: ')
        try:
            find_file(target_dir, size)
        except Exception as e:
            logging.error(e)

    elif choice == "4":
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
                logging.error('Пустой ввод. Программа прервана. Повторите ввод заново')
            else:
                logging.warning('Ошибка ввода. Повторите ввод заново. Выполняется выход из программы')
                return
        except Exception as e:
            
            logging.error(e)
    elif choice == "11":
        try:
            # Валидация происходит ЗДЕСЬ
            v1 = float(input('Введите x: ')) 
            v2 = float(input('Введите y: '))
            
            # Передаем уже ЧИСТЫЕ данные в логику
            print(f"Результат: {add(v1, v2)}")
            
        except ValueError:
            logging.error("Критическая ошибка: Вы ввели не число! Попробуйте еще раз.")
                
    else:
        logging.error("Ошибка: такого варианта нет. Попробуйте снова!")

# Магическая проверка: запущен ли файл напрямую
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("\nПрограмма принудительно завершена пользователем.")
    except Exception as e:
        logging.error(f"Упс! Произошла непредвиденная ошибка: {e}")
                