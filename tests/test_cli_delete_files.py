
from pathlib import Path

path = Path('путь/к/вашему/объекту')

assert not path.exists()



from src.filesystem.cli_delete_files import delete_path

def test_delete_files_dir(tmp_path):
    # 1. Создаем структуру файлов во временной корневой директории
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для функции)
    # 1.1.  Создаем 1-ю папку для проверки работы функции 
    # по удалению папки целиком вместе с файлом 
    base_dir = Path(tmp_path) / "sub"
    base_dir.mkdir()
    # 1.2 Создаем 2-ю папку для проверки работы функции 
    # по удалению ТОЛЬКО файла
    base_dir1 = Path(tmp_path) / "sub1"
    base_dir1.mkdir()

    # 1.1. Создаем файл
    # Файл 1: Маленький (50 Б) - лежит в корне и должен попасть в выборку
    file_small = base_dir / "small.txt"
    file_small.write_bytes(b"0" * 50)
    
    file_small1 = base_dir1 / "small_1.txt"
    file_small1.write_bytes(b"0" * 50)
    # 2. Вызываем функцию 
     ## 2.1. Убеждаемся, что папка или файл удалены
         
    # 2.1.1. Проверяем, что  при указании в  функции delete_path пути к папке:
    # удалена целиком папка
       # Вызываем функцию с путем к папке
    delete_path(base_dir)

    assert not (tmp_path / 'sub').exists()
    
    #  2.1.2 Проверяем, что  при указании в  функции delete_path пути к папке:
    # удален файл
       # Вызываем функцию с путем к файлу 
    delete_path(base_dir1)

    assert not (tmp_path / 'sub1'/"small_1.txt").exists()