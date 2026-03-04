import argparse
import flet as ft 
import os
import logging
from logic_save_to_csv import save_to_csv
from src.filesystem.cli_star_ficha import star_ficha
from chek_path import chek

def star_gui(page: ft.Page):  
    
# 1. Настройка "холста"
    page.title = "Анализатор" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='Путь',   hint_text='Введите путь к директории')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    hello_text = ft.Text(value = "Анализатор директории готов к работе\nРежим ожидания ввода пути к директории",  size=20, color="blue")


## 2. Задаем  функции кнопок:
### 2.1.  Создаем функцию Кнопки btn_select выбора папки из Windows   
    def on_dialog_result(e):  # Выбор из Windows
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            
            path = os.path.normpath(str(text_path.value))
            page.session.set('result', path)
            
        else:
            # Если нажали отмену - не даем программе упасть 
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!


### 2.2.  Функция Кнопки, которая ВВОД:
    def on_button_click_1(e): # Ввод
                       
        path = os.path.normpath(str(text_path.value))
        
        try:
            real_path = chek(path)
   
            text_path.helper_text = "✅ Путь успешно выбран"
            page.session.set('result', real_path)
            hello_text.value = 'Нажмите кнопку\nЗапуск Анализатора'
            hello_text.color = "green"
                    
            #делаем невидимыми поле для ввода пути и кнопку Ввод
            text_path.visible = False
            btn1.visible = False
            # делаем видимым кнопку  Запуск Анализатора
            btn.visible = True
            # после нажатия на кнопку "Ввод" делаем невидимой кнопку Выбора папкиЖ
            btn_select.visible = False
        except Exception as e: 
            
            hello_text.value= "⚠️ Ошибка в имени пути. Проверьте выбор"
            hello_text.color = "yellow"
            text_path.helper_text = "⚠️ Проверьте правильность ввода пути"
            text_path.helper_style = ft.TextStyle(color="red")
            
    
        page.update()

### 2.3.  Кнопки Запуска Анализа:
    ## формируем контейнер для сбора данных в полосе прокрутки
    result_container = ft.Column(
    width=800,         # Ширина области
    height=400,        # Высота области (настройка  под  экран)
    scroll=ft.ScrollMode.ALWAYS, # Всегда показывать полосу прокрутки
    controls=[]        # Сюда мы будем "подкладывать" наш текст
)
    def on_button_click(e): # Запуск Анализатора
        try:
            # забираем из page.session путь записанный в функции on_button_click_1
            res = page.session.get('result')
            # запускаем функцию star_ficha, которую мы импортировали из cli_star_ficha
            fresh_result = star_ficha(res)
            # собираем  вывод res (общая длинная строка) в список 
            ## из отдельных строк по разделителю '\n'
            res_list = fresh_result.split('\n')
        
            page.session.set('res_list', res_list)
        
            # делаем видимой кнопку вывода в файл
            btn2.visible = True
            # Формируем надпись под выводимыми данными
            hello_text.value = "РЕЗУЛЬТАТ"
            hello_text.color = 'red'
            hello_text.size = 30
            # Очищаем контейнер перед новым выводом
            result_container.controls.clear()
            # Добавляем наш результат  в полосу прокрутки (можно вернуть крупный шрифт!)
            
            result_container.controls.append(
                ft.Text(value=fresh_result, size=20, color="green", font_family="Consolas")
            )
            # Скрываем кнопку запуска
            btn.visible = False
        except Exception as err:
            result_container.controls.append(ft.Text(f"❌ Ошибка: {err}", color="red"))
        
        page.update()
        
### 2.4. Собираем функцию Кнопки Вывода в scv
    def on_button_click_2(e): # Вывод в scv
        hello_text.value = "✅ Отчет сохранен в report.scv!"
        # получаем из page.session сохраненный в функции путь к папке 
        res_list = page.session.get('res_list')
        # вызываем функцию save_to_csv, импортированную из файла logic-save_to_csv.py
        save_to_csv(res_list)
        # Прячем кнопку Вывод  в scv
        btn2.visible = False
        page.update()
        
### 2.5. Собираем функцию Кнопки Сброс
    def reset_app(e): # Сброс
        
        hello_text.value = "Анализатор директории готов к работе\nРежим ожидания ввода пути к директории"
        hello_text.color = 'blue'
        page.session.set(None, None)
        text_path.color = "blue"
        text_path.value = None
        # возвращаем видимость кнопки и поля для ввода пути к директории
        text_path.visible = True
        btn1.visible = True
        # прячем кнопку вывода в файл csv
        btn2.visible = False
        # открываем кнопку Выбор Папки:
        btn_select.visible = True
        # прячем строку "text_path.helper_text"
        text_path.helper_text = ''
        # удаляем содержимое окна прокрутки
        result_container.controls.clear()
        
        page.update()
      
### 3.              РАЗДЕЛ  - задание ВСЕХ кнопок  

### 3.1. Задание Кнопки "Запуск Анализатора" (функция on_button_click)
    btn = ft.ElevatedButton("Запуск Анализатора",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_button_click,
                            tooltip="Кнопка для запуска Анализа выбранной папки")  
    btn.visible = False
### 3.2. Задание Кнопки "Ввод" (функция on_button_click_1)
    btn1 = ft.ElevatedButton('ВВОД', icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_button_click_1,
                             tooltip="Кнопка для подтверждения выбранной папки для анализа")  

### 3.3. Задание  Кнопки для  вывода результата в файл csv (функция on_button_click_2)
         
    btn2 = ft.ElevatedButton("Вывод Анализа в csv", icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_button_click_2,
                             tooltip="Вывод Результатов Анализа в файл csv")  
    btn2.visible = False

### 3.4. Задание Кнопки Сброс  (функция reset_app)      
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, on_click=reset_app,
                                  tooltip="Кнопка для сброса и перевода окна в готовность к работе")
### 3.5. Задание Кнопки выбора папки  Windows (функция on_dialog_result)
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.icons.FOLDER_OPEN,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" #  тултип
    )  

### 4. Добавляем элементы графики на страницу Окна -  метод .add() с кортежем *controls
    page.add(text_path, ft.Row([btn1, btn_select], spacing=20),
            
        ft.Row([btn, btn2, btn_reset], alignment=ft.MainAxisAlignment.CENTER, spacing=20 ),
        ft.Row(
            [hello_text],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([result_container], alignment=ft.MainAxisAlignment.CENTER)

            ) 

#### 5. Вызов функции 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    
    args = parser.parse_args()
    
    try:
     ft.app(target=star_gui)
    except Exception as e:
        logging.error(e)

