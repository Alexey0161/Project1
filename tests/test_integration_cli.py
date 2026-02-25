import cli
import sys
from cli import main
from src.filesystem.cli_cnt_files import count_files



def test_cli_command(tmp_path, monkeypatch):
    
    
       # 1. Создаем структуру файлов во временной папке
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для вашей функции)
    base_dir = tmp_path / "project"
    base_dir.mkdir()

    (base_dir / "file1.py").write_text("print('hello')")
    (base_dir / "file2.txt").write_text("some text")

    sub_dir = base_dir / "images"
    sub_dir.mkdir()
    (sub_dir / "logo.txt").write_text("\x00")  # Текстовый файл
    print(base_dir, 22)
    # Имитация argv
    monkeypatch.setattr(sys, 'argv', ['cli.py', 'count', str(base_dir)])
    
    # импортируйте ваш основной модуль или вызовите функцию
    etalon_count_tmp_path = 3

    
    
    result = main()#count_files(str(base_dir))
    # result = count_files(str(base_dir))
    
    print(result, 33)
    
    assert result == etalon_count_tmp_path 
    