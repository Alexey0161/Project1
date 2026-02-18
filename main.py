import argparse
import sys
import logging
# импортируем функции фичей из соответствующих файлов
from src.filesystem.cli_copy_files import copy_file

def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить копировальщик файлов")
    print("2. Запустить счетчик файлов")
    print("3. Запустить поисковик файлов")
    print("4. Запустить установщик даты в имя файла")

    choice = input("Введите номер: ")
    if choice == "1":
        print('----Запускает копировальщик файлов ----')
        try:
            filename = input('Введите имя файла, который надо скопировать: ')
            copy_file(filename)
        except Exception as e:
                
                print(e)

# Магическая проверка: запущен ли файл напрямую
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("\nПрограмма принудительно завершена пользователем.")
    except Exception as e:
        logging.error(f"Упс! Произошла непредвиденная ошибка: {e}")