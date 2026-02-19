r""" --- чтобы в комментарии можно было писать любые пути через слэш "\", не экранируя
Документация:
запуск файла из командной строки из папки src:
 python cli_find_file.py find <путь до целевой папки> <верхний предел размера файла в Кбайтах>
 Пример:
    python cli_find_file.py find /storage/emulated/0/python/tests 100
"""

import os
import sys
import logging

def find_file(target_dir, size):
    target_dir = os.path.normpath(target_dir)
    limit_size = None
    try:
        limit_size = float(size) * 1024 #преобразуем кбайты в байты
    except (ValueError, TypeError):
        print('Вводимое значение должно содержать только цифры')
        
    t = [] # создаем список для файлов, которые прошли фильтр
    if  os.path.exists(target_dir): # через if защищаем код, от падения, если пути не сущенствует
                
        for r, d, f in os.walk(target_dir):
            for i in f: # f - walk выдает файлы в виде списка

                path_i = os.path.join(r,i) # соединяем черз инструмент path
                                        # путь и имя файла
                if os.path.isfile(path_i):

                    full_size = os.path.getsize(path_i)

                    if  limit_size is not None:
                        if full_size < limit_size:
                            t.append(i)
                            logging.info(f'Найден файл: {i} {full_size / 1024: .2f}')
                    else:
                        return
                         
    else: 
        raise FileNotFoundError(f"Ошибка: Путь {target_dir} не существует.")
        
    return t



if __name__ == '__main__':

    if len(sys.argv)  >= 2:
        find_file(sys.argv[1], sys.argv[2])
    else:
        logging.warning("Используйте: python cli.py  <имя_папки> <размер>")

