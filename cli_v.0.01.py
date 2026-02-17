import argparse
import sys
from src.calculator import add
from src.filesystem.cli_cnt_files import count_files
from src.filesystem.cli_modif_files_2 import process_logic

def main():
    # Создаем парсер — он сам создаст тот самый --help!
    parser = argparse.ArgumentParser(description="Project1: Набор полезных утилит")
    
    # Создаем "под-команды" (как в git: git commit, git push)
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Команда 1: Калькулятор
    calc_parser = subparsers.add_parser('calc', help='Сложить два числа')
    calc_parser.add_argument('x', type=float, help='Первое число')
    calc_parser.add_argument('y', type=float, help='Второе число')

    # Команда 2: Счетчик файлов
    count_parser = subparsers.add_parser('count', help='Посчитать файлы в папке')
    count_parser.add_argument('path', type=str, help='Путь к папке')

    # Команда 3: Переименование (дата)
    rename_parser = subparsers.add_parser('rename', help='Добавить дату к именам файлов')
    rename_parser.add_argument('path', type=str, help='Путь к папке')
    rename_parser.add_argument('--recursive', action='store_true', help='Обходить вложенные папки')

    # Разбираем аргументы
    args = parser.parse_args()

    # Выполняем логику (Пункт 3 и 4: ввели один раз — получили результат — выход)
    if args.command == 'calc':
        print(f"Результат: {add(args.x, args.y)}")
    elif args.command == 'count':
        count_files(args.path)
    elif args.command == 'rename':
        process_logic(args.path, args.recursive)
    else:
        # Если команда не введена, выводим справку (Пункт 1)
        parser.print_help()

if __name__ == "__main__":
    main()