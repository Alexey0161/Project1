from pathlib import Path
import logging
import os

def chek_analize(path):
    if not path.value:
        path.value = 'a'               
    path = os.path.normpath(str(path.value))
    real_path = Path(path)
    
    if real_path.exists() and real_path.is_dir() and real_path != 'a':
        return real_path
            
    else:
        logging.warning("Директория не существует.")
        raise FileNotFoundError("⚠️Путь не существует или не является директорией или пустой\n⚠️ Ошибка в имени пути. Проверьте выбор")
