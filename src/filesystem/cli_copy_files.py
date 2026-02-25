"""
    Документация по элементам кода:
        Что делает `os.path.join()`?

        - Это функция из модуля `os.path`, предназначенная для **безопасного и корректного объединения компонентов путей**.
        - Она принимает несколько строковых аргументов, каждый из которых — часть пути, и объединяет их в один путь.
        # Важная особенность: она **учитывает особенности операционной системы**, например, #разделители путей ("/" для Linux/Mac, "\" для Windows).
        ### Почему именно `os.path.join()`?

        - В отличие от простого сложения строк, `os.path.join()` **автоматически вставляет правильный разделитель пути**.
        - Также он **обеспечивает переносимость** кода между разными ОС.

    """

import os
import sys
import shutil
import logging

# def copy_file(filename):
#     base_path = os.getcwd() 
#     src_path = os.path.join(base_path, filename)

#     # 1. Проверка существования оригинала
#     if not os.path.isfile(src_path):
#         logging.warning(f"Файл {filename} не найден в {base_path}")
#         return

#     # 2. Правильное разделение имени (берем только имя, без пути!)
#     just_name = os.path.basename(src_path)
#     name_part, extension = os.path.splitext(just_name)
    
#     # 3. Формируем путь назначения
#     new_filename = f"{name_part}_copy{extension}"
#     dst_path = os.path.join(base_path, new_filename)

#     # 4. Проверка: не существует ли уже копия?
#     if os.path.exists(dst_path):
#         logging.warning(f"Файл {new_filename} уже существует.")
#         return

#     try:
#         # Используем профессиональный инструмент
#         shutil.copy2(src_path, dst_path)
#         logging.info(f"Файл {filename} успешно скопирован в {new_filename}")
#     except Exception as e:
#         logging.error(f"Не удалось скопировать файл: {e}")


# if __name__ == "__main__":
   
#     # Проверяем, что скрипт запущен напрямую, а не импортирован как модуль
#     try:
#     # Проверяем, что передано достаточно аргументов командной строки
      
#         if len(sys.argv) < 2:
#             raise ValueError("Ошибка в количестве аргументов. Правильное использование: <python cli_copy_files.py>  <имя_файла>")
#         filename = sys.argv[1]

#     # Вызов функции копирования файла
#         copy_file(filename)
#     except ValueError as e:
#         # Если аргументов меньше 2 (скрипт, имя файла), выводим инструкцию
        
#         logging.error(e)

def copy_file(filepath):
    src_path = filepath

    # 1. Проверка существования оригинала
    if not os.path.isfile(src_path):
        logging.warning(f"Файл {src_path} не найден")
        return

    # 2. Правильное разделение имени
    just_name = os.path.basename(src_path)
    name_part, extension = os.path.splitext(just_name)

    # 3. Формируем путь назначения
    dir_name = os.path.dirname(src_path)
    new_filename = f"{name_part}_copy{extension}"
    dst_path = os.path.join(dir_name, new_filename)

    # 4. Проверка: не существует ли уже копия
    if os.path.exists(dst_path):
        logging.warning(f"Файл {new_filename} уже существует.")
        return

    try:
        shutil.copy2(src_path, dst_path)
        logging.info(f"Файл {just_name} успешно скопирован в {new_filename}")
    except Exception as e:
        logging.error(f"Не удалось скопировать файл: {e}")
        
if __name__ == "__main__":
   
    # Проверяем, что скрипт запущен напрямую, а не импортирован как модуль
    try:
    # Проверяем, что передано достаточно аргументов командной строки
      
        if len(sys.argv) < 2:
            raise ValueError("Ошибка в количестве аргументов. Правильное использование: <python cli_copy_files.py>  <имя_файла>")
        filename = sys.argv[1]
        logging.info('Файл успешно скопирован')

    # Вызов функции копирования файла
        copy_file(filename)
    except ValueError as e:
        # Если аргументов меньше 2 (скрипт, имя файла), выводим инструкцию
        
        logging.error(e)