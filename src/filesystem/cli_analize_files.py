import os
import logging
import argparse

#  собираем вспомогательную функцию для поиска ключа по пути к файлу
def find_folder_file(folder_path,file_path):
    file_path_norm = os.path.normpath(file_path)
    folder_path_norm = os.path.normpath(folder_path)
    file_parts = file_path_norm.split(os.sep)
    folder_parts = folder_path_norm.split(os.sep)
    file_parts_folder = file_parts[ : len(folder_parts)]
    rel_path_file_folder = os.sep.join(file_parts_folder)
    
    return rel_path_file_folder
       
def calculate_everything(path):
    total = 0
    # создаем словарь для вложенных папок и их размеров
    dict_for_dir = {}
    # создаем словарь для файлов, находящихся в корне директорий
    dict_for_dirfiles = {}
    # создаем общий словарь total_dict для вывода из функции одного отчета, словарь
        ### содержит ключи total - общий размер директории
        ### ключ dict_for_dir - вложенный словарь для вложенных папок и их значений их размеров
        ### ключ dict_for_dirfiles - вложенный словарь для имен файлов, внутри директории и их размеров
    total_dict = {}
     # создаем в словаре dict_for_dir ключ dirs  - и значение - вложенный словарь из 
    #  с ключами - имена вложенных папок, значения - размер папок 
    for root, dirs, files in os.walk(path):
        if root == path:
            # собираем словарь файлов, находящихся в корне директории
            for f in files:
                    fp = os.path.join(root, f)
                    size_file = os.path.getsize(fp)
                    total += size_file # прибавляе размер файла внутри директории к общему размеру директории
                    # добавляем  в словарь  dict_for_dirfiles,  вложенный в словарь total_dict, файлы и их размеры
                    dict_for_dirfiles[f] = size_file
            for folder in dirs:
                # собираем путь к корневым папкам
                folder_path = os.path.join(root, folder)
                # собираем ключи слолваря dict_for_dir
                dict_for_dir[folder_path] = 0

        else:
            # проверяем, что в подпапке есть файлы
            if files:
                file_path = os.path.join(root, files[0])
                
                # определяем ключ родильтельской папки словаря dict_for_dir
                current_parent_key = find_folder_file(folder_path, file_path)
                for f in files:
                    fp = os.path.join(root, f)
                    size_file = os.path.getsize(fp)
                    total += size_file
                    dict_for_dir[current_parent_key] += size_file
   # добавляем в словарь dict_for_dir:
        #  переменную ключ - переменная total, значение - полный объем директории, 
        # посчитанный в total
    total_dict['total'] = total
        # вложенный словарь в качестве ключа название dict_for_dirfiles: 
        # значения - содержания словаря, то есть имена файлов и их размер
    total_dict['dict_for_dirfiles'] = dict_for_dirfiles
    total_dict['dict_for_dir'] = dict_for_dir
    print(total_dict, 64)
    return total_dict

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

        # Распаковка единого отчета по составляющим
        total_dict = calculate_everything(root_path)# вызываю функцию get_dir_size один раз!!!!
        full_size = total_dict['total']
        dict_for_dir = total_dict['dict_for_dir']
        dict_for_dirfiles = total_dict['dict_for_dirfiles']
        
        
        # выводим полный размер директории
     
        print(f'full size: {format_size(full_size):>20}')
        
        #  проверяем есть ли в директории вложенные папки 
        if dict_for_dir: 
            for key, value in dict_for_dir.items():
                #  вырезаем из пути к папке:key имя папки для читаемого отображения 
                    ###   в выводе
                name_folder = os.path.basename(key)
                #   выводим по установленной форме имя вложенной папки и размер, через 
                    ###   функцию format_size переведенных в kb, mb, gb и т.п.
               
                print(f'-folder: {name_folder:<10}  {format_size(value):>10}')
        #  проверяем есть ли в КОРНЕ директории вложенные файлы
        if dict_for_dirfiles:
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
               