import argparse
import flet as ft 
import os
import logging
from src.filesystem.cli_find_file import find_file



def find_gui(page: ft.Page):  
    
# 1. Настройка "холста"
    page.title = "Поисковик" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='ВЫБЕРИТЕ папку через Проводник через кнопку "ВЫБРАТЬ ПАПКУ"',   hint_text='Путь')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    number_input = ft.TextField(label='Введите число --> предельный размер файла',   hint_text='Число', keyboard_type=ft.KeyboardType.NUMBER, width=200)

    hello_text = ft.Text(value = "Поисковик файлов по критерию: меньше заданного размера готов к работе\nРежим ожидания ввода пути к папке и предельного размера файла",  size=20, color="blue")
 
 ## 2. Задаем  функции кнопок:

### 2.1. Задаем функцию Выбора папки 
    def on_dialog_result(e):  # Выбор из Windows
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "                     Путь выбран ----> Выберите предельный размер файла:\n                                               - введите число"
            hello_text.color = "red"
            hello_text.size = 30
            path = os.path.normpath(str(text_path.value))
            page.session.set('directory', path)
            # убираем кнопку выбора из windows
            # btn_select.visible = False
            # # делаем видимыми кнопки выбора режима Рекурсии:
            # btn_confirm.visible = True
            # # делаем видимым Ползунок выбора режима Рекурсии
            # btn_switch.visible = True
            # # делаем видимой кнопку Сброс
            # btn_reset.visible = True
            
        else:
            # Если нажали отмену - не даем программе упасть 
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!
### 2.1. Задаем функцию Кнопки выбора предельного размера файла:
    
    def on_confirm(e):
        # Получаем значение из поля
        value = number_input.value
        try:
            num = float(value)  # или int(value), если нужно целое число
            # здесь можно добавить обработку введенного числа
            print(f"Введено число: {num}")
        except ValueError:
            # Обработка неправильного ввода
            page.window_alert("Пожалуйста, введите корректное число.")
#  ## 3.              РАЗДЕЛ  - задание ВСЕХ кнопок  
    ### 3.1. Задание Кнопки выбора файла из проводника  Windows (функция on_dialog_result)
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.icons.FOLDER_OPEN, visible=True,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" #  тултип
                                    )
    ### 3.2 Задаем Кнопку Подтвердить ввод числа
    btn_confirm = ft.ElevatedButton(text="Подтвердить", on_click=on_confirm)
### 4. Добавляем элементы графики на страницу Окна -  метод .add() с кортежем *controls
 
    page.add(ft.Column([text_path, ft.Row([btn_select,  number_input, btn_confirm], spacing=20), ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER)], 
                
                       expand=True) # Заставляет Column занять всю высоту окна),
                # ft.Container(
                    # content=ft.Column([btn_switch, btn_confirm, btn_modif, btn_reset], spacing=10),
                    # padding=ft.padding.only(left=20, top=20)
                #),
                
           )
        
 
 #### 5. Вызов функции 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    
    args = parser.parse_args()
    
    try:
     ft.app(target=find_gui)
    except Exception as e:
        logging.error(e)