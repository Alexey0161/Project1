from pathlib import  Path
from datetime import date
import os

from cli_modif_files import modif_files
today = date.today()
def test_modif_files_dir(tmp_path, capsys):
    # today = date.today()
        # 1. Создаем структуру файлов во временной папке
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для вашей функции)
    base_dir = tmp_path / "project"
    base_dir.mkdir()
    print(type(str(base_dir)), 13)

    (base_dir / "file1.py").write_text("print('hello')")
    (base_dir / "file2.txt").write_text("some text")

    sub_dir = base_dir / "images"
    sub_dir.mkdir()
    (sub_dir / "logo.txt").write_text("\x00")  # Текстовый файл
    new_files = [f"file1_{today}.py", f"file2_{today}.txt", f"logo_{today}.txt"]


    # 3. Перехватываем вывод
    # captured = capsys.readouterr()
    
    # 4. Проверяем результат
    # Мы создали 3 файла (2 в корне + 1 во вложенной папке)
    
    # # 4.1. Вызываем функцию
    modif_files(str(base_dir))
    
    # 4. Проходим по дереву tmp_....  и проверяем, что в имена добавились даты
    for p, d, f in os.walk(tmp_path):
        for i in f:
            assert i in new_files
    
def test_modif_files_single(tmp_path):
    file_single = tmp_path/'single_file.txt'
    file_single.write_text("Hello, this is a test file")
    print(file_single, 41)
    new_single_file = f'single_file_{today}'
    modif_files(str(file_single))
    assert file_single == new_single_file
        