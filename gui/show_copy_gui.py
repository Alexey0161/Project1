import argparse
import flet as ft
import os
import logging
from src.filesystem.cli_copy_files import copy_file

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
            hello_text.value = "Файл выбран ----> Нажмите Кнопку Копировать файл"
            hello_text.color = "green"
            hello_text.size = 30
            path = os.path.normpath(str(selected_path))
            page.session.set('directory', path)
            # открываем кнопку Копировать
            btn_copy.visible = True
            # прячем кнопку Выбор файла
            btn_select.visible = False
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
### 2.2. Собираем функцию кнопки Копировать файл
    def on_button_copy(e):
        
        try:
            # забираем из page.session путь записанный в функции on_dialog_result
            res = page.session.get('directory')
            copy_file(res)
          # убираем кнопку Удалить папку
            btn_select.visible = False            
                      
            # записываем результат Счетчика в поле для вывода в Окне
            
            ##  "                 РЕЗУЛЬТАТ\n     Удаление объектов произведено\n
            # Нажмите кнопку Срос для перевода Окна в режим готовности"
            hello_text.value = """                 
                                            РЕЗУЛЬТАТ
                                    
                            Копирование файла  произведено
            Нажмите кнопку Срос для перевода Окна в режим готовности"""
            hello_text.color = 'orange'
            hello_text.size = 30
            # btn_find.visible = False
        except Exception as err:
            err = f'''                          ⚠️ Ошибка: {err}
            
            Выберите другой файл для копирования, для чего нажмите кнопку Сброс'''
            hello_text.value = err
            hello_text.color = "red"        
        
        # После удаления закрываем диалог
        page.update()
### 2.5. Собираем функцию кнопки Сброс
    def reset_app(e): # Сброс
        
        hello_text.value = "Удалитель папок  готов к работе \n\nРежим ожидания ввода пути к папке"
 
        hello_text.color = "green"
        hello_text.size = 30
        page.session.set(None, None)
        text_path.color = "blue"
        text_path.value = None
        # возвращаем видимость кнопки и поля для ввода пути к директории
        text_path.visible = True

        # открываем кнопку Выбор Папки:
        btn_select.visible = True
        # прячем строку "text_path.helper_text"
        text_path.helper_text = ''
        # прячем кнопку Удалитель папок
        btn_copy.visible = False
        page.update()      
 ###  2.6. Собираем функцию Кнопки Домой 
    def on_home(e):
        from run_gui import main_show
        page.clean() # очищаем экран от элементов графики Звездочки
        main_show(page) # вызываем Главное Меню/Единое окно
        page.update()       
    page.update()
    
    ## 3. Задание ВСЕХ кнопок
    ### 3.1. Кнопка выбора файла
    btn_select = ft.ElevatedButton(
        "Выбрать файл",  # Изменил текст с "папку" на "файл"
        icon=ft.icons.FOLDER_OPEN, 
        visible=True,
        on_click=open_file_picker,  # Правильно привязываем функцию
        tooltip="Нажмите, чтобы выбрать файл через проводник Windows"
                                    )
#### 3.2. Задание Кнопки  Удаление
    btn_copy = ft.ElevatedButton(text="Копировать файл", visible=False, bgcolor="green", color="white", on_click=on_button_copy)
### 3.3. Задание Кнопки Сброс  (функция reset_app)      
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, visible=True, on_click=reset_app,
                                  tooltip="Кнопка для сброса и перевода окна в готовность к работе")
 ### 3.4.  Задание Кнопки Домой     
    btn_home = ft.ElevatedButton("ДОМОЙ", icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_home,
        tooltip="Нажмите, чтобы перейти в Главное меню выбора фичей") #  тултип
    btn_home.visible = True
    
    ### 4. Добавляем элементы графики
    page.add(
        ft.Column(
            [
                text_path, 
                ft.Row([btn_select, btn_copy, btn_reset], spacing=20),  # Добавил обе кнопки
                ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER), 
                        ft.Container(expand=True),
            ft.Container(
                    content=ft.Row([btn_home], alignment=ft.MainAxisAlignment.END),
                    padding=ft.padding.only(right=20, bottom=50),
                            )
 
            ],
            expand=True
        )
    )

    

#### 5. Вызов функции 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копируем файл")
    args = parser.parse_args()
    
    try:
        ft.app(target=copy_gui)
    except Exception as e:
        logging.error(e)
    