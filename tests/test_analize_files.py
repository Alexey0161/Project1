from pathlib import  Path



from src.filesystem.cli_analize_files import calculate_everything

def test_modif_files_dir(tmp_path):
    # 1. Создаем структуру файлов во временной корневой директории
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для функции)
    base_dir = Path(tmp_path) / "sub"
    base_dir.mkdir()

    # 1.1. Создаем файл
    # Файл 1: Маленький (50 Б) - лежит в корне и должен попасть в выборку
    file_small = base_dir / "small.txt"
    file_small.write_bytes(b"0" * 50)
    
    # 2.  Создаем вложенную папку "images" в корневой директории "sub"
    sub_dir = base_dir / "images" 
    sub_dir.mkdir()
    # 2.1. Создаем два Больших файла (150 Б), размер котрых должен просуммироваться, но сами файлы 
    # - не должен попасть в вывод
    file_large = sub_dir / "large.txt"
    file_large.write_bytes(b"0" * 150)
    file_large1 = sub_dir / "large1.txt"
    file_large1.write_bytes(b"0" * 250)
    

    
    # 3. Собираем эталонный вывод функции, с которым мы будем сравнивать вывод реально
    ## отработавшей функции
    etalon_total_dict = {'total': 450, 'dict_for_dirfiles': {"small.txt" : 50}, 'dict_for_dir': {str(sub_dir): 400}}

    # 4. Вызываем функцию
    # 4.1. Проверяем соответствие вывода функции calculate_everything с etalon_total_dict
    assert calculate_everything(str(base_dir)) == etalon_total_dict
    