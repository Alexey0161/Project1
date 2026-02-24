from pathlib import  Path
from datetime import datetime
import os

from src.filesystem.cli_modif_files import process_logic

# today = date.today()
def test_modif_files_dir(tmp_path, recursive=None):
    # today = date.today()
    stats = os.stat(tmp_path)
    formatted_date = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d')
        
        # 1. Создаем структуру файлов во временной папке
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для вашей функции)
    base_dir = tmp_path / "project"
    base_dir.mkdir()
    # print(type(str(base_dir)), 13)

    (base_dir / "file1.py").write_text("print('hello')")
    (base_dir / "file2.txt").write_text("some text")

    sub_dir = base_dir / "images"
    sub_dir.mkdir()
    (sub_dir / "logo.txt").write_text("\x00")  # Текстовый файл
    # new_files = [f"file1_{today}.py", f"file2_{today}.txt", f"logo_{today}.txt"]
    new_files_recursive = [f"file1_{formatted_date}.py", f"file2_{formatted_date}.txt", f"logo_{formatted_date}.txt"]
    new_files = [f"file1_{formatted_date}.py", f"file2_{formatted_date}.txt"]


    #### 3. Перехватываем вывод
    # captured = capsys.readouterr()
    
    # 4. Проверяем результат
    # Мы создали 3 файла (2 в корне + 1 во вложенной папке)
    
    # # 4.1. Вызываем функцию
    if recursive:
        process_logic(str(base_dir), recursive)
        for root, dirs, files in os.walk(base_dir):
            for i in files:
                assert i in process_logic(str(base_dir))
    else:
        process_logic(str(base_dir))
    
    # 4. Проходим по дереву tmp_....  и проверяем, что в имена добавились даты
        for  f in os.listdir(base_dir):
            if os.path.isfile(f):
                print(f, 40)
                # for i in f:
                assert f in new_files
        # from pathlib import Path

        # directory = tmp_path  # текущая директория

        # # Получаем объекты файлов в директории
        # files = [f for f in directory.iterdir() if f.is_file()]

        # print("Только файлы (используя pathlib):")
        # for file in files:
        #     print(file.name)
        
# def test_modif_files_single(tmp_path):
#     file_single = tmp_path/'single_file.txt'
#     file_single.write_text("Hello, this is a test file")
#     # print(file_single, 41)
#     new_single_file = f'single_file_{today}'
#     process_logic(str(file_single))
#     assert file_single == new_single_file
        