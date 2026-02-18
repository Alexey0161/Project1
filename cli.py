import argparse
import logging
# импортируем функцию интерактивного меню из файла main.py
from main import main as start_interactive
# импортируем функции фичей из соответствующих файлов
from src.filesystem.cli_copy_files import copy_file

# Импортируем модуль логирования
import logging

# Настройка "голоса"  программы в логировании
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S' # Чтобы не загромождать дату, оставим только время
)

def main():
    parser = argparse.ArgumentParser(description="Project1: Универсальный инструмент")
    subparsers = parser.add_subparsers(dest="command", help="Команды")

    # --- КОМАНДА ДЛЯ ДУШИ (Ваше меню) делаем add_parser для меню---
    menu_parser = subparsers.add_parser('menu', help='Запустить интерактивный интерфейс')

       # --- КОМАНДЫ ДЛЯ ТЗ (Утилиты) ---

    # Команда 1: Копирователь файла
    copy_p = subparsers.add_parser('copy', help='Скопировать файл')
    copy_p.add_argument('file_name', type=str, help='Имя файла, который нужно найти и скопировать')

    
    args = parser.parse_args()
    
        # ЛОГИКА ВЫБОРА
    if args.command == 'menu':
        start_menu()  # Запускаем интерактивное меню!
    elif args.command == 'copy':
        copy_file(args.file_name)

    else:
        parser.print_help()

def start_menu():
    print("--- Добро пожаловать в Интерактивный Режим! ---")
    start_interactive()
    # Тут  старый код с input(), choice и while True
    # Это ваша "песочница", ТЗ её не запрещает, если она вызывается отдельно!


if __name__ == "__main__":
    main()