import argparse
import logging
import os

from src.config import BYTES_PER_KB, setup_logging


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
    dict_for_dir = {}
    dict_for_dirfiles = {}

    total_dict = {}
    for root, dirs, files in os.walk(path):
        if root == path:
            for f in files:
                    fp = os.path.join(root, f)
                    size_file = os.path.getsize(fp)
                    total += size_file # прибавляе размер файла внутри директории к общему размеру директории
                    dict_for_dirfiles[f] = size_file
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                dict_for_dir[folder_path] = 0

        else:
            # проверяем, что в подпапке есть файлы
            if files:
                file_path = os.path.join(root, files[0])

                current_parent_key = find_folder_file(folder_path, file_path)
                for f in files:
                    fp = os.path.join(root, f)
                    size_file = os.path.getsize(fp)
                    total += size_file
                    dict_for_dir[current_parent_key] += size_file
    total_dict['total'] = total
    total_dict['dict_for_dirfiles'] = dict_for_dirfiles
    total_dict['dict_for_dir'] = dict_for_dir

    return total_dict

def format_size(size_bytes):
    dict_size = {}
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)
    unit_index = 0
    while size >= BYTES_PER_KB and unit_index < len(units) - 1:
        size /= BYTES_PER_KB
        unit_index += 1
    # Форматируем результат с 2 знаками после запятой
    if units[unit_index] == 'bytes':
        return f"{int(size)} {units[unit_index]}"
    else:
        return f"{size:.2f} {units[unit_index]}"
    # Основной алгоритм анализе:
def star_ficha(root_path):

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
        result_str = format_size(full_size)

        print(f'full size: {result_str:>20}')
        result = f'full size: {result_str:>20}\n'

        #  проверяем есть ли в директории вложенные папки
        if dict_for_dir:

            for key, value in dict_for_dir.items():

                name_folder = os.path.basename(key)

                result_str = format_size(value)

                 # вычисляем процент занимаего места от полного размера папки
                part_size = round((value/full_size)*100, 2)
                print(f'-folder: {name_folder:<10}  {result_str:>10} amounts to {part_size}% ')
                result += f'-folder: {name_folder:<10}  {result_str:>10} amounts to {part_size}%\n'


        # #  проверяем есть ли в КОРНЕ директории вложенные файлы
        if dict_for_dirfiles:
            for key, value in dict_for_dirfiles.items():
                result_str = format_size(value)

                 # вычисляем процент занимаего места от полного размера папки
                part_size = round((value/full_size)*100, 2)

                print(f'-file: {key:<10} {result_str:>10} amounts to {part_size}% ')
                result += f'-file: {key:<10} {result_str:>10} amounts to {part_size}%\n'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    parser.add_argument("path", help="Путь к папке")

    args = parser.parse_args()

    try:

       setup_logging()
       star_ficha(args.path)
    except Exception as e:
        logging.error(e)
