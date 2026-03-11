import argparse
import flet as ft 
import os
import logging
from src.filesystem.cli_cnt_files import count_files


def count_gui(page: ft.Page):  
    
# 1. Настройка "холста"
    page.title = "Поисковик" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='ВЫБЕРИТЕ папку через Проводник через кнопку "ВЫБРАТЬ ПАПКУ"',   hint_text='Путь')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    result_count = ft.Text( size=100, color="orange")
    result_count.visible = False
    hello_text = ft.Text(value = "Счетчик количества файлов в папке готов к работе\nРежим ожидания ввода пути к папке",  size=20, color="blue")
 
 ## 2. Собираем  функции кнопок:

### 2.1. Собираем функцию Выбора папки 
    def on_dialog_result(e):  # Выбор из Windows
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "                     Путь выбран ----> Нажмите кнопку Запуск счетчика"
            hello_text.color = "green"
            hello_text.size = 30
            path = os.path.normpath(str(text_path.value))
            page.session.set('directory', path)
            # убираем кнопку выбора из windows
            btn_select.visible = False
            btn_count.visible = True

            
            
        else:
            # Если нажали отмену - не даем программе упасть 
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!

### 2.2. Собираем функцию кнопки запуска Счетчика

    def on_button_count(e): # Запуск Поисковика
        try:
            # забираем из page.session путь записанный в функции on_dialog_result
            res = page.session.get('directory')
                        # убираем кнопку Запуск Счетчик
            btn_count.visible = False            
            # запускаем функцию find_file, которую мы импортировали из cli_find_file
            fresh_result = count_files(res)
            result_count.visible = True
            # записываем результат Счетчика в поле для вывода в Окне
            result_count.value = fresh_result
            hello_text.value = "РЕЗУЛЬТАТ\n           "
            hello_text.color = 'red'
            hello_text.size = 30
            # btn_find.visible = False
        except Exception as err:
            err = f"❌ Ошибка: {err}"
            result_count.value = err
            result_count.color = "red"
        page.update()
### 2.4. Собираем функцию кнопки Сброс
    def reset_app(e): # Сброс
        
        hello_text.value = "Счетчик количества файлов в папке готов к работе\nРежим ожидания ввода пути к папке"
 
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
        # обнуляем строку 
        result_count.value = ''
        result_count.color = 'orange'
        # обнуляем строку 
        result_count.helper_text = ''
        result_count.helper_style = ft.TextStyle(color="blue")
        
        
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
    ### 3.2. Задаем кнопку функции запуск Счетчика:
    btn_count = ft.ElevatedButton("Запуск Счетчика",  icon=ft.icons.PLAY_ARROW_SHARP, visible = False, on_click=on_button_count,
                            tooltip="Кнопка для запуска Поисковика файлов в  выбранной папке")  

    ### 3.3. Задание Кнопки Сброс  (функция reset_app)      
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, visible=True, on_click=reset_app,
                                  tooltip="Кнопка для сброса и перевода окна в готовность к работе")

 ### 3.4.  Задание Кнопки Домой     
    btn_home = ft.ElevatedButton("ДОМОЙ", icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_home,
        tooltip="Нажмите, чтобы перейти в Главное меню выбора фичей") #  тултип
    btn_home.visible = True
   
### 4. Добавляем элементы графики на страницу Окна -  метод .add() с кортежем *controls
 
    page.add(
        ft.Column(
        [
        text_path, ft.Row([btn_select, btn_count, btn_reset], spacing=20), 
             ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([result_count], alignment=ft.MainAxisAlignment.CENTER),
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
     ft.app(target=count_gui)
    except Exception as e:
        logging.error(e)