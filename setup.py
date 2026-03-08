from setuptools import setup, find_packages

setup(
    name="my_super_project",         # Название вашей библиотеки
    version="0.1.0",                 # Версия
    packages=find_packages(),        # Автоматически найдет папку src
    py_modules=["cli"],             # Включаем наш файл cli.py
    install_requires=[               # Если бы у вас были внешние библиотеки (например, pandas)
        # 'requests', 
    ],
    entry_points={                   # САМЫЙ ВАЖНЫЙ ПУНКТ В блоке entry_points мы прописали:

                                    # my-cool-tool — это имя команды, 
                                    # которую вы будете вводить в терминале. Вы можете заменить его на любое другое (например, supertool).

                                    # cli :main — это путь: имя_файла:имя_функции. 
                                    # Мы говорим системе: «Когда пользователь 
                                    # введет my-cool-tool, найди файл cli.py 
                                    # и запусти в нем функцию main()».
        'console_scripts': [
            'my-cool-tool = cli:main', 
        ],
    },
)