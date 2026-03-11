import argparse
import flet as ft
import os
import logging
from src.filesystem.cli_delete_files import delete_path

def delete_gui(page: ft.Page):

    # 1. Настройка "холста"
    page.title = "Удалитель папок и файлов" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='ВЫБЕРИТЕ папку через Проводник через кнопку "ВЫБРАТЬ ПАПКУ"',   hint_text='Путь')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    
    hello_text = ft.Text(value = "Удалитель папок и  файлов готов к работе \nРежим ожидания ввода пути к папке",  size=30, color="green")

 ## 2. Собираем  функции кнопок:
### 2.1. Собираем функцию Выбора папки 
    def on_dialog_result(e):  # Выбор из Windows
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "                     Путь выбран ----> Нажмите Кнопку Удалить папку \n                     и далее следуйте инструкциям диалогового окна"
            hello_text.color = "green"
            hello_text.size = 30
            path = os.path.normpath(str(text_path.value))
            page.session.set('directory', path)
            # убираем кнопку выбора из windows
            btn_select.visible = False
            # открываем кнопку Удалить папку:
            btn_delete.visible = True
            
            
            
        else:
            # Если нажали отмену - не даем программе упасть 
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!
    ### 2.2.  Функции для управления диалогом
    def show_dialog(e):
        page.dialog = alert
        alert.open = True
        page.update()

    def close_dialog(e):
        alert.open = False
        page.update()
    ### 2.3. Собираем функцию кнопки Удалить папк
    def confirm_delete(e):
        # Вызываем  бэкенд для удаления
        try:
            # забираем из page.session путь записанный в функции on_dialog_result
            res = page.session.get('directory')
            delete_path(res)
          # убираем кнопку Удалить папку
            btn_delete.visible = False            
                  
            # записываем результат Счетчика в поле для вывода в Окне
            
            ## = "                 РЕЗУЛЬТАТ\n     Удаление объектов произведено\n
            # Нажмите кнопку Срос для перевода Окна в режим готовности"
            hello_text.value = """                 
                                    РЕЗУЛЬТАТ
                            Удаление объектов произведено
            Нажмите кнопку Срос для перевода Окна в режим готовности"""
            hello_text.color = 'red'
            hello_text.size = 30
            # btn_find.visible = False
        except Exception as err:
            err = f"❌ Ошибка: {err}"
            hello_text.value = err
            hello_text.color = "red"        
        
        # После удаления закрываем диалог
        alert.open = False
        page.update()
    ### 2.4. Создаём диалог один раз при инициализации
    alert = ft.AlertDialog(
        title=ft.Text("Подтверждение удаления"),
        content=ft.Text("Вы уверены, что хотите удалить папку?"),
        actions=[
            ft.TextButton("Отмена", on_click=lambda e: close_dialog(e)),
            ft.TextButton("Удалить", on_click=confirm_delete),
                ],
                        )
### 2.4. Собираем функцию кнопки Сброс
    def reset_app(e): # Сброс
        
        hello_text.value = "Удалитель папок и  файлов готов к работе \nРежим ожидания ввода пути к папке"
 
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
        btn_delete.visible = False
        
        
        page.update()      

#  ## 3.              РАЗДЕЛ  - задание ВСЕХ кнопок  
    ### 3.1. Задание Кнопки выбора файла из проводника  Windows (функция on_dialog_result)
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.icons.FOLDER_OPEN, visible=True,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" #  тултип
                                    )
    # ### 3.2. Задание Кнопки  Удаление
    btn_delete = ft.ElevatedButton(text="УДАЛИТЬ ПАПКУ", visible=False, bgcolor="red", color="white", on_click=show_dialog)
    
     ### 3.3. Задание Кнопки Сброс  (функция reset_app)      
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, visible=True, on_click=reset_app,
                                  tooltip="Кнопка для сброса и перевода окна в готовность к работе")


### 4. Добавляем элементы графики на страницу Окна -  метод .add() с кортежем *controls
 
    page.add(
        
        text_path, ft.Row([btn_select, btn_delete, btn_reset], spacing=20),
        ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER), 

            )

#### 5. Вызов функции 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    args = parser.parse_args()
    
    try:
        ft.app(target=delete_gui)
    except Exception as e:
        logging.error(e)
