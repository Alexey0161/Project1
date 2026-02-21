import os
import logging
import sys
import argparse

def get_dir_size(path):
    cnt = 0
    total = 0
    total_local = {}
    
    dict_for_dir = {}
    for root, dirs, files in os.walk(path):
        name = os.path.basename(root)
        # print(name, dirs, files, 14)
        if cnt == 0 and len(dirs) > 0:
            for i in dirs:
                dict_for_dir[i] = [0]
            # print(dict_for_dir, 18)
        
        for f in files:
            fp = os.path.join(root, f)
            size_file = os.path.getsize(fp)
            total += size_file
            # print(total, 23)
            # for j in dict_for_dir.keys():
            #     if j in root:
            #         print(total,25)
            #         dict_for_dir[j].append(total)
            if cnt > 0:
                for j in dict_for_dir.keys():
                    # print(j,25)
                    if j in root:
                        # print(total,31)
                        dict_for_dir[j].append(size_file)
        cnt += 1
        # if cnt == 3:
            
            
    # print(dict_for_dir,38)
    for k in dict_for_dir.keys():
        dict_for_dir[k] = sum(dict_for_dir[k])
    # print(dict_for_dir,40)

    return total, dict_for_dir#, total_local

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
        result = get_dir_size(root_path)#[0], get_dir_size(root_path)[1]
        full_size = result[0]
        dict_for_dir = result[1]
        # print(full_size, 54)
        # print(dict_for_dir, 55)
        # print(total_local, 48)
        print(f'full size: {format_size(full_size)}')
        for item in os.listdir(root_path):
            # print(item,75)
            full_path = os.path.join(root_path, item)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                print(f'-file: {item:<10} {format_size(size):>10}')
            else:

            #         print(item, 56)
            #         pass
            #         print(f'-folder: {item:<10}  {format_size(dict_folder[item]):>10}') # редактирую сейчас
                size = dict_for_dir[item] # Вот она, магия анализа вложенности!
                print(f'-folder: {item:<10}  {format_size(size):>10}')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    parser.add_argument("path", help="Путь к папке")
   
    args = parser.parse_args()
    
    try:
       analize_files(args.path)
    except Exception as e:
        logging.error(e)
               