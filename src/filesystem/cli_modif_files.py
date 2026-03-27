import argparse
import logging
import os
from datetime import datetime



def rename_file_with_date(file_path):
    """Вспомогательная функция для переименования одного файла"""
    # try: убрал этот блок, чтобы ошибка всплывала в Графику и там отображалась
    stats = os.stat(file_path)
    formatted_date = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d')
    directory = os.path.dirname(file_path)
    name, ext = os.path.splitext(os.path.basename(file_path))
    
    if formatted_date in name:
        msg = f"дата уже присутствует"
        logging.warning(f"Пропуск файла {name}: {msg}.")
        
        raise ValueError(msg)

    else:
        new_name = f"{name}_{formatted_date}{ext}"
        new_path = os.path.join(directory, new_name)

        logging.info(f'Меняем: {name}{ext} --> {new_name}')
        os.rename(file_path, new_path)
    # except Exception as e: убрал этот блок, чтобы ошибка всплывала в Графику и там отображалась
    #     logging.warning(f"Ошибка при обработке {file_path}: {e}")

def process_logic(root_path, recursive=None):
    errors = []
    """Основная логика обхода, которая не зависит от argparse"""
    root_path = os.path.normpath(root_path)
    if not os.path.exists(root_path): # через if защищаем код, от падения, если пути не сущенствует

            raise FileNotFoundError(f"Ошибка: Путь {root_path} не существует.")
    elif recursive:

        for p, d, f in os.walk(root_path):
            for i in f:
                print(f, 44)
                full_path = os.path.join(p, i)
                try:
                    rename_file_with_date(full_path)
                except Exception as e:
                    filename = os.path.basename(full_path)
                    # Форматируем ошибку красиво для "мешка"
                    errors.append(f"[{filename}]: {e}")
                    logging.error(f"Отказ: дата в имени файла уже есть {filename}: {e}")

    else:

        for i in os.listdir(root_path):
            
            full_path = os.path.join(root_path, i)
            if os.path.isfile(full_path):
                
                try:
                    rename_file_with_date(full_path)
                except Exception as e:
                    filename = os.path.basename(full_path)
                    # Форматируем ошибку красиво для "мешка"
                    errors.append(f"[{filename}]: {e}")
                    
                    logging.error(f"Отказ: дата в имени файла уже есть {filename}: {e}")
    # После цикла решаем судьбу "мешка"
    if errors:
        # Собираем всё в одну большую строку для Графики
        summary_error = "Проблемы с файлами:\n" + "\n".join(errors)
        
        raise Exception(summary_error)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Добавляет дату к именам файлов")
    parser.add_argument("command", choices=["modif"], help="Команда для выполнения.")
    parser.add_argument("path", help="Путь к папке")

    parser.add_argument("--recursive", action="store_true", help="Обходить вложенные папки")

    args = parser.parse_args()
    try:
        if args.command == "modif":
            process_logic(args.path, args.recursive)
    except Exception as e:
        logging.error(e)
