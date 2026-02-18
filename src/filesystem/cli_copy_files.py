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
import logging


# def copy_file(filename):
#     # Привязка к директории, из которой пользователь запускает фичу :
#     base_path = os.getcwd() 
  
#     # Формируем полный путь к файлу, который нужно скопировать
#     file_path = os.path.join(base_path, filename)
#     # Объединяем  директорию  с именем файла, чтобы получить полный путь

#     # Проверяем, существует ли указанный файл по данному 
    
#     if not os.path.exists(file_path):
#         # Если файла нет, выводим сообщение и завершаем функцию
#         logging.warning(f"Файл {filename} не найден в {base_path}")
#         return


#     # Формируем полный путь к файлу назначения
#        # собираем новое имя для копии
#            # разделяем имя и расширение
#     name, ext = os.path.splitext(file_path)
    
#     destination_path = os.path.join(base_path, f'{name}_copy.{ext}')
#     try:
#         with open(destination_path, 'x') as file:
#             pass
            
#     except FileExistsError:
#         logging.warning('Файл уже существует.')
#         return

#     # Открываем исходный файл для чтения в бинарном режиме
#     with open(file_path, 'rb') as src:
#         # Открываем файл назначения для записи в бинарном режиме
#         with open(destination_path, 'wb') as dst:
#             # Читаем содержимое исходного файла и записываем его в файл назначения
#             dst.write(src.read())

#     # Выводим сообщение о завершении копирования
#     logging.info(f"Файл {filename} скопирован ")

import os
import shutil
import logging

def copy_file(filename):
    base_path = os.getcwd() 
    src_path = os.path.join(base_path, filename)

    # 1. Проверка существования оригинала
    if not os.path.isfile(src_path):
        logging.warning(f"Файл {filename} не найден в {base_path}")
        return

    # 2. Правильное разделение имени (берем только имя, без пути!)
    just_name = os.path.basename(src_path)
    name_part, extension = os.path.splitext(just_name)
    
    # 3. Формируем путь назначения
    new_filename = f"{name_part}_copy{extension}"
    dst_path = os.path.join(base_path, new_filename)

    # 4. Проверка: не существует ли уже копия?
    if os.path.exists(dst_path):
        logging.warning(f"Файл {new_filename} уже существует.")
        return

    try:
        # Используем профессиональный инструмент
        shutil.copy2(src_path, dst_path)
        logging.info(f"Файл {filename} успешно скопирован в {new_filename}")
    except Exception as e:
        logging.error(f"Не удалось скопировать файл: {e}")


if __name__ == "__main__":
   
    # Проверяем, что скрипт запущен напрямую, а не импортирован как модуль
    try:
    # Проверяем, что передано достаточно аргументов командной строки
      
        if len(sys.argv) < 2:
            raise ValueError("Ошибка в количестве аргументов. Правильное использование: <python cli_copy_files.py>  <имя_файла>")
        filename = sys.argv[1]

    # Вызов функции копирования файла
        copy_file(filename)
    except ValueError as e:
        # Если аргументов меньше 2 (скрипт, имя файла), выводим инструкцию
        
        logging.error(e)
        
