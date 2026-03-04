from pathlib import Path
import logging

def chek(path):
    real_path = Path(path)
    if real_path.exists() and real_path.is_dir():
        return real_path
            # logging.warning("Директория существует.")
    else:
        logging.warning("Директория не существует. 9999999")
        raise FileNotFoundError("Путь не существует или не является директорией")
        
        