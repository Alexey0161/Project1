import os
import logging
import argparse

def calculate_everything(path):
    
    total = 0
    # создаем словарь для вложенных папок и их размеров
    dict_for_dir = {}
    # создаем словарь для файлов, находящихся в корне директорий
    dict_for_dirfiles = {}
    walk = os.walk(path)
    first_step = next(walk)
    root_first, dirs_first, files_first = first_step
    if len(dirs_first) != 0:
        #  Собираем словарь с ключами в виде названий вложенных папок
        for i in dirs_first:
            i_p = os.path.join(root_first, i)
            dict_for_dir[i_p] = [0]
    # проверяем есть ли в корне директории файлы:
    if len(files_first) != 0:
        # собираем словарь из файлов директории: ключ - имя файла, значение - размер файла
        
        for j in files_first:
            # собираем полный путь к файлу из пути к директории + имя файла
            j_p = os.path.join(root_first, j)
            # вычисляем размер файла 
            size_dir_file = os.path.getsize(j_p)
            # добавляем размер файлов, находящихся в корне директории 
            # к общему размеру директории
            total += size_dir_file
            # собираем словарь, в котором ключи - названия файлов, значения - размер файлов в байтах
            dict_for_dirfiles[j] = size_dir_file
    
    for root, dirs, files in walk:

        for f in files:
            fp = os.path.join(root, f)
            size_file = os.path.getsize(fp)
            total += size_file
            for j in dict_for_dir.keys():
                if j in root:
                    # формируем словарь, в котором ключами будут имена вложенных папок 
                    dict_for_dir[j].append(size_file)
    # суммируем значения размеров файлов в папках по ключам, которыми являются имена папок
    for k in dict_for_dir.keys():
        dict_for_dir[k] = sum(dict_for_dir[k])


    return total, dict_for_dir, dict_for_dirfiles

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
    if not os.path.exists(root_path): # через if защищаем код, от падения, если пути не сущенствует
        
            raise FileNotFoundError(f"Ошибка: Путь {root_path} не существует.")
    else:
        result = calculate_everything(root_path)# вызываю функцию get_dir_size один раз!!!!
        full_size = result[0]
        dict_for_dir = result[1]

        dict_for_dirfiles = result[2]
        # выводим полный размер директории
        print(f'full size: {format_size(full_size):>20}')
        
        # проверяем есть ли в директории вложенные папки 
        if len(dict_for_dir) != 0: 
            for key, value in dict_for_dir.items():
                #  вырезаем из пути к папке:key имя папки для читаемого отображения 
                #   в выводе
                name_folder = os.path.basename(key)
                #   выводим по установленной форме имя вложенной папки и размер, через 
                #   функцию format_size переведенных в kb, mb, gb и т.п.
                print(f'-folder: {name_folder:<10}  {format_size(value):>10}')
        # проверяем есть ли в директории вложенные файлы
        if len(dict_for_dirfiles) != 0:
            for key, value in dict_for_dirfiles.items():
                #   выводим по установленной форме имя вложенной папки и размер, через 
                #   функцию format_size переведенных в kb, mb, gb и т.п.
                print(f'-file: {key:<10} {format_size(value):>10}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    parser.add_argument("path", help="Путь к папке")
   
    args = parser.parse_args()
    
    try:
       analize_files(args.path)
    except Exception as e:
        logging.error(e)
               