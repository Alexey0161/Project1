

import os
import sys
import logging
# import config
from config import BYTES_PER_KB 

def find_file(target_dir, size):
    target_dir = os.path.normpath(target_dir)
    # print(target_dir, size, 9)
    limit_size = None
    try:
        limit_size = float(size) * BYTES_PER_KB  #преобразуем кбайты в байты
    except (ValueError, TypeError):
        print('Ошибка: Вводимое значение должно содержать только цифры')
        
    found_files = [] 
    if  os.path.exists(target_dir): # через if защищаем код, от падения, если пути не сущенствует
                
        for r, d, f in os.walk(target_dir):
            for i in f: # f - walk выдает файлы в виде списка

                path_i = os.path.join(r,i) # соединяем черз инструмент path
                                        # путь и имя файла
                if os.path.isfile(path_i):

                    full_size = os.path.getsize(path_i)
                    # print(full_size, 27)

                    if  limit_size is not None:
                        if full_size < limit_size:
                            found_files.append(i)
                            logging.info(f'Найден файл: {i} {full_size / BYTES_PER_KB: .2f}')
                            print(f'Найден файл: {i} {full_size / 1024: .2f}')
                    else:
                        return
        # print(found_files, 35)                         
    else: 
        raise FileNotFoundError(f"Ошибка: Путь {target_dir} не существует.")
        
    return found_files

find_file('C:\\Users\\ivano\\Desktop\\Project1\\Total1', 1)

# if __name__ == '__main__':

#     if len(sys.argv)  >= 2:
#         find_file(sys.argv[1], sys.argv[2])
#     else:
#         logging.warning("Используйте: python cli.py  <имя_папки> <размер>")

