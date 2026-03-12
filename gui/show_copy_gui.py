import argparse
import flet as ft
import os
import logging
from src.filesystem.cli_delete_files import delete_path

import flet as ft
import os

def copy_gui(page: ft.Page):

    # 1. Настройка "холста"
    page.title = "Копирователь файлов" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='ВЫБЕРИТЕ файл через Проводник через кнопку "ВЫБРАТЬ ФАЙЛ"', hint_text='Путь')
    text_path.visible = True
    
    hello_text = ft.Text(value="Копирователь файлов готов к работе \nРежим ожидания ввода пути к файлу", size=30, color="green")


    ## 2. Собираем функции кнопок:
    ### 2.1. Собираем функцию Выбора файла
    def on_dialog_result(e):  # Выбор из Windows
        if e.files:  # Для файлов берем e.files, то есть список с объектом [FilePickerFile(name='proba_total1.txt', path='C:\\Users\\ivano\\Desktop\\Project1\\Total1\\proba_total1.txt', size=129)]  
            
            # Выбран файл
            selected_path = e.files[0].path  # Берем путь, включащий файл из объекта FilePickerFile
            text_path.value = selected_path
            text_path.helper_text = "✅ Файл успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "Файл выбран ----> Нажмите Кнопку Удалить"
            hello_text.color = "green"
            hello_text.size = 30
            path = os.path.normpath(str(selected_path))
            page.session.set('directory', path)
            # убираем кнопку выбора
            
        else:
            # Если нажали отмену
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()

    # Создаем диалог выбора файлов
    get_file_dialog = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(get_file_dialog)
    # Функция для открытия диалога выбора файла
    def open_file_picker(e):
        get_file_dialog.pick_files(
            dialog_title="Выберите файл",
            allow_multiple=False,
            allowed_extensions=None,
            file_type=ft.FilePickerFileType.ANY,
            initial_directory=os.path.expanduser("~")
        )

    ## 3. Задание ВСЕХ кнопок
    ### 3.1. Кнопка выбора файла
    btn_select = ft.ElevatedButton(
        "Выбрать файл",  # Изменил текст с "папку" на "файл"
        icon=ft.icons.FOLDER_OPEN, 
        visible=True,
        on_click=open_file_picker,  # Правильно привязываем функцию
        tooltip="Нажмите, чтобы выбрать файл через проводник Windows"
    )
    


    ## 4. Добавляем элементы графики
    page.add(
        ft.Column(
            [
                text_path, 
                ft.Row([btn_select], spacing=20),  # Добавил обе кнопки
                ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER), 
            ],
            expand=True
        )
    )

    

#### 5. Вызов функции 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    args = parser.parse_args()
    
    try:
        ft.app(target=copy_gui)
    except Exception as e:
        logging.error(e)
    