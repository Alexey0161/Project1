r""" --- чтобы в комментарии можно было писать любые пути через слэш "\", не экранируя
Документация:
запуск файла из командной строки из папки src:
 python cli_find_file.py find <путь до целевой папки> <верхний предел размера файла в Кбайтах>
 Пример:
    python cli_find_file.py find /storage/emulated/0/python/tests 100
"""

import os
import sys


def find_file(target_dir, size):
    limit_size = int(size) * 1024 #преобразуем кбайты в байты
    t = [] # создаем список для файлов, которые прошли фильтр
    for r, d, f in os.walk(target_dir):
        for i in f: # f - walk выдает файлы в виде списка

            path_i = os.path.join(r,i) # соединяем черз инструмент path
                                       # путь и имя файла
            if os.path.isfile(path_i):

                full_size = os.path.getsize(path_i)

                if full_size < limit_size:
                    t.append(i)
                    print(f'Найден файл: {i} {full_size / 1024: .2f}')
    return t



if __name__ == '__main__':

    if len(sys.argv)  == 3 and sys.argv[1]  == 'find':
        find_file(sys.argv[2], sys.argv[3])

