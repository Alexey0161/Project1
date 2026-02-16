r'''
Документация:
на 15.02.26 Остановился на корректировке файла cli_modif_files.py  
проверил запуск через --recursive  и без него. Все работает.
Также написал файл test_cli_modif_files.py, но в нем только базовая 
логика без условия --recursive, а по условию, если путь передан как  
папка или файл, что ошибка, так как в задании на проект этого нет.
Запуск файла из терминала из папки, проверил на src, командой: 
python cli_modif_files.py C:\Users\ivano\Desktop\Project1\src\destination
или командой:
python cli_modif_files.py C:\Users\ivano\Desktop\Project1\src\destination 
-- recursive
'''

import os
import re, sys
import argparse

from datetime import datetime

# собираем фильтр по именам файлов по наличию расширения
pattern = r'.+\.[A-Za-z0-9]+$'

def modif_files(root_path):
    
    parser = argparse.ArgumentParser(description="Добавляет дату к именам файлов")
    
    # Путь к папке (обязательный аргумент)
    parser.add_argument("root_path", help="Путь к папке или файлу")
    
    # Тот самый ключ! action="store_true" значит: если ключ есть, значение будет True
    parser.add_argument("--recursive", action="store_true", help="Обходить вложенные папки")

    args = parser.parse_args()
    
    if args.recursive is True:
        for p, d, f in os.walk(root_path):
            for i in f:
                if re.match(pattern,i): # фильтруем имена файлов по наличию расширения
                
                    # Склеиваем путь: папка + имя файла
                    full_path = os.path.join(p, i) 
                    
                    try:
                        stats = os.stat(full_path)
                        # 1. Получаем секунды
                        creation_seconds = stats.st_ctime 
        
        # 2. Переводим секунды в объект даты
                        dt_object = datetime.fromtimestamp(creation_seconds)
        
        # 3. Форматируем в строку (ГГГГ-ММ-ДД)
                        formatted_date = dt_object.strftime('%Y-%m-%d')
                        
                        name, ext = os.path.splitext(full_path)
        # Собираем новое имя
                        new_name = f"{os.path.basename(name)}_{formatted_date}{ext}"
                        print(f'Старое имя: {os.path.basename(name)} меняем --> {new_name}')
                        full_path_modif = os.path.join(p, new_name)
                        os.rename(full_path, full_path_modif)
                    except FileNotFoundError:
                        print(f"Ошибка: Файл {i} не найден по пути {full_path}")
    
    else:
        print(os.path.basename(root_path), 52)
        try:
            for i in os.listdir(root_path):
                full_path = os.path.join(root_path, i)
                
                
                if os.path.isfile(full_path):
                    print(777777)
                    
                    stats = os.stat(full_path)
                    
                                    # 1. Получаем секунды
                    creation_seconds = stats.st_ctime 
                    
                    # 2. Переводим секунды в объект даты
                    dt_object = datetime.fromtimestamp(creation_seconds)
                    
                    # 3. Форматируем в строку (ГГГГ-ММ-ДД)
                    formatted_date = dt_object.strftime('%Y-%m-%d')
                                    
                    name, ext = os.path.splitext(full_path)
                    # Собираем новое имя
                    new_name = f"{os.path.basename(name)}_{formatted_date}{ext}"
                    print(f'Старое имя: {os.path.basename(name)} меняем --> {new_name}')                                
                    new_full_path = os.path.join(root_path, new_name)
                    os.rename(full_path, new_full_path)
        except FileNotFoundError as e:
                e = f"Ошибка: директория {os.path.basename(root_path)} не найдена"

                print(e)

# modif_files(root_path)
# modif_files('cli_find_file.py')                                      
if __name__ == '__main__':
        
    if len(sys.argv) >= 2:
        modif_files(sys.argv[1])


