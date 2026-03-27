import logging
import os
import sys

from src.config import BYTES_PER_KB, setup_logging


def find_file(target_dir, size):
    target_dir = os.path.normpath(target_dir)
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

                    if  limit_size is not None:

                        if full_size < limit_size:
                            
                            found_files.append(i)
                            print(f'Найден файл: {i} {full_size / BYTES_PER_KB: .2f}', 36)
                            
                    else:
                        return
    else:
        raise FileNotFoundError(f"Ошибка: Путь {target_dir} не существует.")
    
    return found_files

if __name__ == '__main__':
    setup_logging()
    if len(sys.argv)  >= 2:
        find_file(sys.argv[1], sys.argv[2])
    else:
        logging.warning("Используйте: python cli.py  <имя_папки> <размер>")

