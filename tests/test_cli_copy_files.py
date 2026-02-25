import shutil
import filecmp
import os
from pathlib import Path

from src.filesystem.cli_copy_files import copy_file

def test_copy_file(tmp_path):
    # 1. Создаем структуру файлов во временной корневой директории
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для функции)
    
    base_dir = Path(tmp_path) / "sub"
    base_dir.mkdir()
    
        # 1.1. Создаем файл
    # Файл : Маленький (50 Б) - лежит в корне и должен попасть в выборку
    file_small = base_dir / "small.txt"
    file_small.write_bytes(b"0" * 50)
    
        # Устанавливаем текущую директорию на наш tmp_path/sub
    original_cwd = os.getcwd()
    os.chdir(base_dir)
    # 2. Создаем эталонное имя файладля проверки работы функции copy
    etalon_name = "small_copy.txt"
    
    
    
        # 3. Вызываем функцию 
     ## 1.1. Убеждаемся, что файл скопирован в той же директории, но с приставкой 
    ## _copy
    try:
        # copy_file("small.txt")
        copy_file(file_small)
    finally:
        os.chdir(original_cwd)
    
    
    for root, dirs, files in os.walk(base_dir):
        
                # Обнаруживаем копию файла
        copied_file_path = base_dir / etalon_name

            # Проверяем, что файл создан
        assert copied_file_path.exists(), "Копия файла не создана"
        
        
        assert filecmp.cmp(file_small, copied_file_path, shallow=False)
        

         
