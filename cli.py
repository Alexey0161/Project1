import argparse
import sys
# Импортируем вашу старую логику меню, если она еще в отдельной функции
# Или просто перенесем код из main.py в функцию start_menu()



def main():
    parser = argparse.ArgumentParser(description="Project1: Универсальный инструмент")
    subparsers = parser.add_subparsers(dest="command", help="Команды")

    # --- КОМАНДА ДЛЯ ДУШИ (Ваше меню) ---
    subparsers.add_argument('menu', help='Запустить интерактивный интерфейс')

    # --- КОМАНДЫ ДЛЯ ТЗ (Утилиты) ---
    # Команда 1: Калькулятор
    calc_p = subparsers.add_parser('calc', help='Сложить два числа')
    calc_p.add_argument('x', type=float, help='Первое число' )
    calc_p.add_argument('y', type=float, help='Второе число')

    # Команда 2: Счетчик файлов
    count_p = subparsers.add_parser('count', help='Посчитать файлы в папке')
    count_p.add_argument('path', type=str, help='Путь к папке'))

    # ... и так далее для всех фич ...
    # Команда 3: Переименование (дата)
    rename_parser = subparsers.add_parser('rename', help='Добавить дату к именам файлов')
    rename_parser.add_argument('path', type=str, help='Путь к папке')
    rename_parser.add_argument('--recursive', action='store_true', help='Обходить вложенные папки')

    args = parser.parse_args()

    # ЛОГИКА ВЫБОРА
    if args.command == 'menu':
        start_menu()  # Запускаем ваш шедевр!
    elif args.command == 'calc':
        from src.calculator import add
        print(f"Результат: {add(args.x, args.y)}")
    elif args.command == 'count':
        from src.filesystem.cli_cnt_files import count_files
        count_files(args.path)
    else:
        # Если ничего не введено или --help
        parser.print_help()

def start_menu():
    print("--- Добро пожаловать в Интерактивный Режим! ---")
    # Тут ваш старый код с input(), choice и while True
    # Это ваша "песочница", ТЗ её не запрещает, если она вызывается отдельно!


if __name__ == "__main__":
    main()