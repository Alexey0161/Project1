# tests/test_calculator.py
r"""
Документация:
запускаются все тесты одной командой из директории, в которой находится проект, то есть C:\Users\ivano\Desktop\Project1>
одной командой:  pytest
"""
import pytest

# # 1. Импортируем нашу функцию из папки src
from calculator import add


# 2. Пишем тестовую функцию, соблюдая правило именования
def test_add():
    #### 3. Используем assert для проверки
    assert add(2, 3) == 5

# #### 3.
# def test_add_with_wrong_expectation():
#     """Этот тест специально написан так, чтобы провалиться."""
#     # Вызываем функцию прямо внутри assert, чтобы увидеть детализацию ошибки
#     assert add(2, 2) == 5

# ... (другие тесты) ...

def test_add_raises_type_error_on_string_input():
    with pytest.raises(TypeError):
        add(5, "hello")
