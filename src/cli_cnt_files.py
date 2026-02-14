r'''
#Документаия к файлу:
#Запуск файла: (my_venv)
PS C:\Users\ivano\Desktop\Project1\src> python cli_cnt_files.py count
C:\Users\ivano\Desktop\Project1\src ,
#то есть из папки src командой с указанием полного пути к папке src:
#python cli_cnt_files.py count C:\Users\ivano\Desktop\Project1\src

'''

import os
import sys


# Допустим, путь к папке мы берем из sys.argv[2]
# python cli.py count folder_name
 # возвращает список введенных имен в комндной строке, то есть 0 - имя вызываемого файла
                         # 1 - выполняемая команда, 2 - путь к папке, с которой  работает функция вызываемеого файла
def count_files(target_dir):
    if not os.path.exists(target_dir): # через if защищаем код, от падения, если пути не сущенствует
        print(f"Ошибка: Путь {target_dir} не существует.")
        return

    total_files = 0 # счетчик файлов

    # root — текущий адрес папки
    # dirs — список подпапок (нам здесь не нужны)
    # files — список файлов в этой конкретной папке
    for root, dirs, files in os.walk(target_dir):
        total_files += len(files)  # Прибавляем количество файлов в текущей папке

    print(f"Всего файлов в '{target_dir}' (включая вложенные): {total_files}")

if __name__ == "__main__":
    # Простая проверка команды
    if len(sys.argv) > 2 and sys.argv[1] == "count":
        count_files(sys.argv[2])
    else:
        print("Используйте: python cli.py count <имя_папки>")


