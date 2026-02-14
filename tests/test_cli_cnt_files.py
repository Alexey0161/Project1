from cli_cnt_files import count_files


def test_count_files_standard_output(tmp_path, capsys):
    """Тестируем, что функция печатает правильное число файлов."""

    # 1. Создаем структуру файлов во временной папке
    # (tmp_path — это путь в виде объекта, поэтому переводим в str для вашей функции)
    base_dir = tmp_path / "project"
    base_dir.mkdir()

    (base_dir / "file1.py").write_text("print('hello')")
    (base_dir / "file2.txt").write_text("some text")

    sub_dir = base_dir / "images"
    sub_dir.mkdir()
    (sub_dir / "logo.txt").write_text("\x00")  # Текстовый файл

    # 2. Вызываем функцию
    count_files(str(base_dir))

    # 3. Перехватываем вывод
    captured = capsys.readouterr()

    # 4. Проверяем результат
    # Мы создали 3 файла (2 в корне + 1 во вложенной папке)
    expected_output = f"Всего файлов в '{base_dir}' (включая вложенные): 3"
    assert expected_output in captured.out


def test_count_files_not_found(capsys):
    """Тестируем реакцию на несуществующую папку."""
    fake_path = "this/path/does/not/exist"

    count_files(fake_path)

    captured = capsys.readouterr()
    assert f"Ошибка: Путь {fake_path} не существует." in captured.out
