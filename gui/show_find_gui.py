import argparse
import logging
import os

import flet as ft
from gui.logic.check_number import check_number
from src.filesystem.cli_find_file import find_file


def find_gui(page: ft.Page):

# 1. Настройка "холста"
    page.title = "Поисковик"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    text_path = ft.TextField(label='ВЫБЕРИТЕ папку через Проводник через кнопку "ВЫБРАТЬ ПАПКУ"',   hint_text='Путь')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    number_input = ft.TextField(label='Введите число --> предельный размер файла',   hint_text='Число', keyboard_type=ft.KeyboardType.NUMBER, width=200)
    number_input.visible = False
    hello_text = ft.Text(value = "Поисковик файлов по критерию: меньше заданного размера готов к работе\nРежим ожидания ввода пути к папке и предельного размера файла",  size=20, color="blue")

 ## 2. Собираем  функции кнопок:

### 2.1. Собираем функцию Выбора папки
    def on_dialog_result(e):  # Выбор из Windows
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "                     Путь выбран ----> Выберите предельный размер файла:\n                                               - введите число"
            hello_text.color = "green"
            hello_text.size = 30
            path = os.path.normpath(str(text_path.value))
            page.session.set('directory', path)
            # убираем кнопку выбора из windows
            btn_select.visible = False
            # # делаем видимыми кнопку подтверждения введенного числа:
            btn_confirm.visible = True
            # # делаем видимым Поле ввода числа:
            number_input.visible = True


        else:
            # Если нажали отмену - не даем программе упасть
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()

    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)

    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!
### 2.2. Собираем функцию Кнопки Подтверждения выбора предельного размера файла:

    def on_confirm(e):
        # Получаем значение из поля
        val = number_input.value
        try:
            value_checked = check_number(val)

            # забираем num  в page.session:
            page.session.set('number', value_checked)
            # здесь можно добавить обработку введенного числа
            btn_find.visible = True
            btn_confirm.visible = False
            btn_select.visible = False
            number_input.visible = False
            hello_text.value = "                     Нажмите кнопку Запуск Поисковика"
            hello_text.color = "green"
            hello_text.size = 30
            print(f"Введено число: {value_checked}")
        except ValueError:

            number_input.helper_text = '⚠️ Ошибка ввода!\nВведите число'
            number_input.helper_style = ft.TextStyle(color="yellow")

        page.update()
### 2.3. Собираем функцию запуска Поисковика

    ## формируем контейнер для сбора данных в полосе прокрутки
    result_container = ft.Column(
    width=800,         # Ширина области
    height=400,        # Высота области (настройка  под  экран)
    scroll=ft.ScrollMode.ALWAYS, # Всегда показывать полосу прокрутки
    controls=[]        # Сюда мы будем "подкладывать" наш текст
)
    def on_button_find(e): # Запуск Поисковика
        try:
            # забираем из page.session путь записанный в функции on_dialog_result
            res = page.session.get('directory')
            # забираем из page.session число записанный в функции on_dialog_result
            num = page.session.get('number')

            # запускаем функцию find_file, которую мы импортировали из cli_find_file
            fresh_result = find_file(res, num)

            hello_text.value = "РЕЗУЛЬТАТ"
            hello_text.color = 'red'
            hello_text.size = 30
            btn_find.visible = False
            result_container.controls.clear()
            # Добавляем наш результат  в полосу прокрутки (можно вернуть крупный шрифт!)

            result_container.controls.append(
                ft.Text(value=fresh_result, size=20, color="green", font_family="Consolas")
            )


        except Exception as err:
            result_container.controls.append(ft.Text(f"❌ Ошибка: {err}", color="red"))
        page.update()
### 2.4. Собираем функцию кнопки Сброс
    def reset_app(e): # Сброс

        hello_text.value = "Поисковик файлов по критерию: меньше заданного размера готов к работе\nРежим ожидания ввода пути к папке и предельного размера файла"
        hello_text.color = "green"
        hello_text.size = 20
        page.session.set(None, None)
        text_path.color = "blue"
        text_path.value = None
        # возвращаем видимость кнопки и поля для ввода пути к директории
        text_path.visible = True

        # открываем кнопку Выбор Папки:
        btn_select.visible = True
        # прячем строку "text_path.helper_text"
        text_path.helper_text = ''
        # обнуляем строку
        number_input.value = ''
        # обнуляем строку
        number_input.helper_text = ''
        number_input.helper_style = ft.TextStyle(color="blue")
        # удаляем содержимое окна прокрутки
        result_container.controls.clear()

        page.update()
    ###  2.5. Собираем функцию Кнопки Домой
    def on_home(e):
        from run_gui import main_show
        page.clean() # очищаем экран от элементов графики Звездочки
        main_show(page) # вызываем Главное Меню/Единое окно
        page.update()
    page.update()

#  ## 3.              РАЗДЕЛ  - задание ВСЕХ кнопок
    ### 3.1. Задание Кнопки выбора файла из проводника  Windows (функция on_dialog_result)
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.icons.FOLDER_OPEN, visible=True,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" #  тултип
                                    )
    ### 3.2 Задаем Кнопку Подтвердить ввод числа
    btn_confirm = ft.ElevatedButton(text="Подтвердить", visible=True, on_click=on_confirm)

    ### 3.3. Задаем кнопку функции запуск Поисковика:
    btn_find = ft.ElevatedButton("Запуск Поисковика",  icon=ft.icons.PLAY_ARROW_SHARP, visible = False, on_click=on_button_find,
                            tooltip="Кнопка для запуска Поисковика файлов в  выбранной папке")
### 3.4. Задание Кнопки Сброс  (функция reset_app)
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, visible=True, on_click=reset_app,
                                  tooltip="Кнопка для сброса и перевода окна в готовность к работе")
### 3.5.  Задание Кнопки Домой
    btn_home = ft.ElevatedButton("ДОМОЙ", icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_home,
        tooltip="Нажмите, чтобы перейти в Главное меню выбора фичей") #  тултип
    btn_home.visible = True


### 4. Добавляем элементы графики на страницу Окна -  метод .add() с кортежем *controls

    page.add(
        ft.Column(
        [
        text_path, ft.Row([btn_select,  number_input, btn_confirm, btn_find], spacing=20),
             ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([btn_reset], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([result_container]),
               ft.Container(expand=True),
                ft.Container(
                    content=ft.Row([btn_home], alignment=ft.MainAxisAlignment.END),
                    padding=ft.padding.only(right=20, bottom=50),
                            )
        ],
            expand=True # Заставляет Column занять всю высоту окна
                    )

            )


 #### 5. Вызов функции
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")

    args = parser.parse_args()

    try:
     ft.app(target=find_gui)
    except Exception as e:
        logging.error(e)
