from setuptools import setup, find_packages

setup(
    name="my_super_project",         # Название вашей библиотеки
    version="0.1.0",                 # Версия
    packages=find_packages(),        # Автоматически найдет папку src
    py_modules=["cli"],             # Включаем наш файл cli.py
    install_requires=[               # Если бы у вас были внешние библиотеки (например, pandas)
        # 'requests', 
    ],
    entry_points={                   # САМЫЙ ВАЖНЫЙ ПУНКТ
        'console_scripts': [
            'my-cool-tool = cli:main', 
        ],
    },
)