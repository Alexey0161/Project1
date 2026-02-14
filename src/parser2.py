"""
Документация:
для запуска парсера, --> перейти в папку, где он находится -->
    1. Вариант запуска с телом функции в командной строке:
            python parser2.py "def add(x, y): return x + y" --func_name add --args 5 8
    2. Вариант запуска с передачей парсеру имени файла, в котором находится функция --> он открывает файл
       2.1. читает содержимое командой <--- для терминала VSCode, то есть PowerShell:
            (Get-Content calculator.py | Out-String)
       Полностью команда выглядит так (проверено ---> работает)
            python parser2.py (Get-Content calculator.py | Out-String) --func_name add --args 5 8
       2.2. читает содержимое командой <--- для терминала bash:
            bash
            "$(cat calculator.py)"
        Полностью команда выглядит так (НЕ ПРОВЕРЕНО):
            bash
            python parser2.py "$(cat calculator.py)" --func_name add --args 5 8
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Универсальный парсер функции. ")
    parser.add_argument('function_code', type=str, help='Код функции или описание для парсинга')
    parser.add_argument('--func_name', type=str, default='my_func', help='Имя функции для вызова')
    parser.add_argument('--args', nargs='*', help='Аргументы для вызова функции', default=[])

    args = parser.parse_args()

    code_str = args.function_code
    function_name = args.func_name
    func_args = args.args

    # Выполняем код
    local_vars = {}
    exec(code_str, {}, local_vars)

    # Проверяем наличие функции
    if function_name in local_vars:
        func = local_vars[function_name]
        # Обработка типов аргументов
        # Предполагается, что все аргументы — это числа или строки
        parsed_args = []
        for arg in func_args:
            # Попытка преобразовать в число
            try:
                parsed_arg = int(arg)
            except ValueError:
                try:
                    parsed_arg = float(arg)
                except ValueError:
                    # Оставляем строкой
                    parsed_arg = arg
            parsed_args.append(parsed_arg)

        # Вызов функции
        result = func(*parsed_args)
        print(f"Результат вызова {function_name}{tuple(parsed_args)}: {result}")

    else:
        print(f"Функция '{function_name}' не найдена в переданном коде.")

if __name__ == "__main__":
    main()
