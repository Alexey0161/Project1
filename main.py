import argparse
import sys
import logging
# импортируем функции фичей из соответствующих файлов
from src.filesystem.cli_copy_files import copy_file
from src.filesystem.cli_cnt_files import count_files
from src.filesystem.cli_find_file import find_file
from src.filesystem.cli_modif_files import process_logic
from src.filesystem.cli_analize_files import analize_files
from src.filesystem.cli_delete_files import delete_path

def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить копировальщик файлов")
    print("2. Запустить удалитель папок и файлво")
    print("3. Запустить счетчик файлов")
    print("4. Запустить поисковик файлов")
    print("5. Запустить установщик даты в имя файла")
    print("6. Запустить анализатор директорий")

    choice = input("Введите номер: ")
    if choice == "1":
        print('----Запускает копировальщик файлов ----')
        try:
            filename = input('Введите имя файла, который надо скопировать: ')
            copy_file(filename)
        except Exception as e:
                
                print(e)
    
    if choice == "2":
        print('----Запускает удалитель папок и  файлов ----')
        try:
            target_path = input('Введите путь: ')
            delete_path(target_path)
        except Exception as e:
                
                print(e)
    
    
    if choice == "3":
        print('----Запускает счетчик файлов ----')
        try:
            target_dir = input('Введите полный путь к директории, в который надо подсчитать количество файлов: ')
            count_files(target_dir)
        except Exception as e:
                
                logging.error(e)
    if choice == "4":
        print('----Запускает поисковик файлов ----')
        try:
            target_dir = input('Введите полный путь к директории, в который надо подсчитать количество файлов: ')
            size = input('Введите значение размера, меньше которого будет размер найденных файлов: ')
            find_file(target_dir, size)
        except Exception as e:
                
                logging.error(e)
    if choice == "5":
        print('----Запускает установщик даты в имя файла ----')
        try:
            target_dir = input('Введите полный путь к директории, в который надо подсчитать количество файлов: ')
            recursive = input('Введите параметр для вложенных папок "--recursive": ')
            process_logic(target_dir, recursive)
        except Exception as e:
            logging.error(e)
        
    if choice == "6":
        print('----Запускает анализатор директории ----')                
        try:
            root_path = input(' Введите полный путь к директории, выбранной для анализа: ')
            analize_files(root_path)
        except Exception as e:
            logging.error(e)
                

# Магическая проверка: запущен ли файл напрямую
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("\nПрограмма принудительно завершена пользователем.")
    except Exception as e:
        logging.error(f"Упс! Произошла непредвиденная ошибка: {e}")