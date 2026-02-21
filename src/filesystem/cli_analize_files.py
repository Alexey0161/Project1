import os
import logging
import sys
import argparse

def get_dir_size(path):
    total = 0
    total_local = 0
    dict_for_dir = {}
    for root, dirs, files in os.walk(path):
        name = os.path.basename(root)
        for f in files:
            fp = os.path.join(root, f)
            total += os.path.getsize(fp)
            total_local += os.path.getsize(fp)
        dict_for_dir[name] = total_local
        total_local = 0

    return total, dict_for_dir

def format_size(size_bytes):
    # Определяем пороги для перехода на следующую единицу
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    # Форматируем результат с 2 знаками после запятой
    if units[unit_index] == 'bytes':
        return f"{int(size)} {units[unit_index]}"
    else:
        return f"{size:.2f} {units[unit_index]}"

# Основной алгоритм анализе:
def analize_files(root_path):
    root_path = os.path.normpath(root_path)
    name = os.path.basename(root_path)
    
    if not os.path.exists(root_path): # через if защищаем код, от падения, если пути не сущенствует
        
            raise FileNotFoundError(f"Ошибка: Путь {root_path} не существует.")
    else:
        
        print(f'full size: {format_size(get_dir_size(root_path)[0])}')
        for item in os.listdir(root_path):
            full_path = os.path.join(root_path, item)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                print(f'-file: {item:<10} {format_size(size):>10}')
            else:
                if item != name:
                    print(f'-folder: {item:<10}  {format_size(get_dir_size(root_path)[1][item]):>10}') # редактирую сейчас
        #         size = get_dir_size(full_path) # Вот она, магия анализа вложенности!
        #         print(f'-folder: {item:<10}  {format_size(size):>10}')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    parser.add_argument("path", help="Путь к папке")
   
    args = parser.parse_args()
    
    try:
       analize_files(args.path)
    except Exception as e:
        logging.error(e)
               