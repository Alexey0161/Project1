# tests/test_calculator.py

# # 1. Импортируем нашу функцию из папки src
from src.calculator import add

# # 2. Пишем тестовую функцию, соблюдая правило именования
# def test_add():
#     # 3. Используем assert для проверки
#     assert add(2, 3) == 5

#### 3.
def test_add_with_wrong_expectation():
    """Этот тест специально написан так, чтобы провалиться."""
    # Вызываем функцию прямо внутри assert, чтобы увидеть детализацию ошибки
    assert add(2, 2) == 5