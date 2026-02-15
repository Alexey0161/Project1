import os
import re, sys

from datetime import datetime

# собираем фильтр по именам файлов по наличию расширения
pattern = r'.+\.[A-Za-z0-9]+$'

def modif_files(root_path):
    if os.path.isdir(root_path):
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
                # вычисляем путь к файлу:
        
        for p, d, f in os.walk('C:/Users/ivano/Desktop/Project1'):
            
            if str(root_path) in f:
                full_path = os.path.join(p, root_path)
                path = p
                
                break
        stats = os.stat(root_path)
        
                        # 1. Получаем секунды
        creation_seconds = stats.st_ctime 
        
        # 2. Переводим секунды в объект даты
        dt_object = datetime.fromtimestamp(creation_seconds)
        
        # 3. Форматируем в строку (ГГГГ-ММ-ДД)
        formatted_date = dt_object.strftime('%Y-%m-%d')
                        
        name, ext = os.path.splitext(root_path)
        # Собираем новое имя
        new_name = f"{os.path.basename(name)}_{formatted_date}{ext}"
        print(f'Старое имя: {os.path.basename(name)} меняем --> {new_name}')                                
        new_full_path = os.path.join(path, new_name)
        os.rename(full_path, new_full_path)

# modif_files(root_path)
# modif_files('cli_find_file.py')                                      
if __name__ == '__main__':
    print(sys.argv[2])
    
    if len(sys.argv) > 2 and sys.argv[1] == 'modif':
        modif_files(sys.argv[2])


