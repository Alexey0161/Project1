import os
import argparse
from datetime import datetime
from pathlib import Path

def rename_file_with_date(file_path):
    """Вспомогательная функция для переименования одного файла"""
    try:
        stats = os.stat(file_path)
        formatted_date = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d')
        
        directory = os.path.dirname(file_path)
        name, ext = os.path.splitext(os.path.basename(file_path))
        if formatted_date in name:
            print('В имени файла уже есть дата создания. Изменения в имя файла не вносятся')
            return
        else:
            new_name = f"{name}_{formatted_date}{ext}"
            new_path = os.path.join(directory, new_name)
            
            print(f'Меняем: {name}{ext} --> {new_name}')
            os.rename(file_path, new_path)
    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}")

def process_logic(root_path, recursive=None):
    """Основная логика обхода, которая не зависит от argparse"""
    root_path = os.path.normpath(root_path)
    if not os.path.exists(root_path): # через if защищаем код, от падения, если пути не сущенствует
        
            raise FileNotFoundError(f"Ошибка: Путь {root_path} не существует.")
    elif recursive:
        for p, d, f in os.walk(root_path):
            for i in f:
                full_path = os.path.join(p, i)
                rename_file_with_date(full_path)
    else:
        
        for i in os.listdir(root_path):
            full_path = os.path.join(root_path, i)
            if os.path.isfile(full_path):
                rename_file_with_date(full_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Добавляет дату к именам файлов")
    parser.add_argument("path", help="Путь к папке")
    parser.add_argument("--recursive", action="store_true", help="Обходить вложенные папки")
    
    args = parser.parse_args()
    try:
        process_logic(args.path, args.recursive)
    except Exception as e:
        print(e)
