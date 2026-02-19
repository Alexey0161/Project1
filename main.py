import argparse
import sys
import logging
# импортируем функции фичей из соответствующих файлов
from src.filesystem.cli_copy_files import copy_file
from src.filesystem.cli_cnt_files import count_files
from src.filesystem.cli_find_file import find_file

def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить копировальщик файлов")
    print("3. Запустить счетчик файлов")
    print("4. Запустить поисковик файлов")
    print("5. Запустить установщик даты в имя файла")

    choice = input("Введите номер: ")
    if choice == "1":
        print('----Запускает копировальщик файлов ----')
        try:
            filename = input('Введите имя файла, который надо скопировать: ')
            copy_file(filename)
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

# Магическая проверка: запущен ли файл напрямую
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("\nПрограмма принудительно завершена пользователем.")
    except Exception as e:
        logging.error(f"Упс! Произошла непредвиденная ошибка: {e}")