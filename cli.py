import argparse
import sys
# Импортируем вашу старую логику меню, если она еще в отдельной функции
# Или просто перенесем код из main.py в функцию start_menu()
from src.calculator import add
from src.filesystem.cli_cnt_files import count_files
from src.filesystem.cli_modif_files import process_logic
from src.main import main as start_interactive
from src.filesystem.cli_find_file import find_file
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
    
    # Команда 2: Счетчик файлов
    count_p = subparsers.add_parser('count', help='Посчитать файлы в папке')
    count_p.add_argument('path', type=str, help='Путь к папке')
    
    # Команда 3: Поисковик файлов по размеру меньше заданной величины
    find_p = subparsers.add_parser('find', help='Найти  файлы в во всех папках директории по размеру меньше заданной величины')
    find_p.add_argument('target_dir', type=str, help='Путь к папке, в которой ищутся файлы')
    find_p.add_argument('size', type=str, help='Задается параметр фильтра по размеру')
    
    # Команда 4: Переименование (дата)
    rename_parser = subparsers.add_parser('rename', help='Добавить дату к именам файлов')
    rename_parser.add_argument('path', type=str, help='Путь к папке')
    rename_parser.add_argument('--recursive', action='store_true', help='Обходить вложенные папки')

    # Команда 11: Калькулятор
    calc_p = subparsers.add_parser('calc', help='Сложить два числа')
    calc_p.add_argument('x', type=float, help='Первое число' )
    calc_p.add_argument('y', type=float, help='Второе число')

    args = parser.parse_args()

    # ЛОГИКА ВЫБОРА
    if args.command == 'menu':
        start_menu()  # Запускаем интерактивное меню!
    elif args.command == 'copy':
        copy_file(args.file_name)
    
    elif args.command == 'count':
        count_files(args.path)
    elif args.command == 'find':
        find_file(args.target_dir, args.size)
    elif args.command == 'rename':
        process_logic(args.path, args.recursive) 
    elif args.command == 'calc':
        print(f"Результат: {add(args.x, args.y)}")  
    else:
        # Если ничего не введено или --help
        parser.print_help()

def start_menu():
    print("--- Добро пожаловать в Интерактивный Режим! ---")
    start_interactive()
    # Тут  старый код с input(), choice и while True
    # Это ваша "песочница", ТЗ её не запрещает, если она вызывается отдельно!


if __name__ == "__main__":
    main()