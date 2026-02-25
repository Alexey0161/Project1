from pathlib import Path

from src.filesystem.cli_find_file import find_file



def test_find_file(tmp_path, capsys):
    # 1. Создаем структуру папок внутри временной директории

    subdir = Path(tmp_path) / "sub"
    subdir.mkdir()

    # 2. Создаем файлы разного размера
    # Файл 1: Маленький (50 КБ) - должен попасть в выборку
    file_small = subdir / "small.txt"
    file_small.write_bytes(b"0" * 50 * 1024)

    # Файл 2: Большой (150 КБ) - не должен попасть
    file_large = subdir / "large.txt"
    file_large.write_bytes(b"0" * 150 * 1024)

        ####### Проверяю почему ошибка:
    # file_small = tmp_path / "small.txt"
    # file_small.write_bytes(b"0" * 10 * 1024)

    ####### завершение проверки

    # Файл 3: Еще один маленький (10 КБ)
    file_tiny = tmp_path / "tiny.txt"
    file_tiny.write_bytes(b"0" * 10 * 1024)



    # 3. Запускаем функцию (порог 100 КБ)
    # Передаем tmp_path как строку, если функция ждет путь
    result = find_file(str(tmp_path), 100)
     # 3.1. Перехватываем вывод
    # result1 = capsys.readouterr()

    # 4. Проверяем результат
    expected = [str(file_small.name), str(file_tiny.name)]
    # expected = [str(file_tiny.name)]

    # Сортируем списки, чтобы тест не падал из-за разного порядка файлов
    assert sorted(result) == sorted(expected)
