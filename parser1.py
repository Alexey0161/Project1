import argparse

def main():
    parser = argparse.ArgumentParser(description="Парсер функции")
    parser.add_argument('function_code', type=str, help='Код функции или описание для парсинга')

    args = parser.parse_args()
    code_str = args.function_code
    print(type(code_str))
    # Выполняем полученный код
    local_vars = {}
    exec(code_str, {}, local_vars)

    # Выводим содержимое для отладки
    print("Объявленные переменные после exec:", list(local_vars.keys()))

    # Предполагаем, что функция называется my_func
    if 'my_func' in local_vars:
        local_vars['my_func']()
    else:
        print("Функция my_func не найдена в переданном коде.")
        # выводим переменные, чтобы понять, что есть
        for key, value in local_vars.items():
            print(f'{key} = {value}')

if __name__ == "__main__":
    main()
