import argparse
import logging
from src.filesystem.cli_copy_files import copy_file

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

    # Здесь пока пусто — команды будем добавлять в feature-ветках!

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()

if __name__ == "__main__":
    main()