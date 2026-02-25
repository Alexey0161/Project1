import argparse
import os
import shutil
import sys

def delete_path(target_path):
    print(target_path, 7)
    # Проверяем, существует ли путь
    if not os.path.exists(target_path):
        print(f"Ошибка: '{target_path}' не существует.")
        sys.exit(1)
    # Если это папка, удаляем рекурсивно
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)
        print(f"Папка '{target_path}' успешно удалена.")
    else:
        os.remove(target_path)
        print(f"Файл '{target_path}' успешно удален.")

def main():
    parser = argparse.ArgumentParser(description="Удаляет файл или папку по имени.")
    parser.add_argument("command", choices=["delete"], help="Команда для выполнения.")
    parser.add_argument("name", help="Путь к файлу или папке, которую нужно удалить.")

    args = parser.parse_args()

    if args.command == "delete":
        delete_path(args.name)

if __name__ == "__main__":
    main()