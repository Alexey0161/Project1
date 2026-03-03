import argparse
import logging
import flet as ft 
import os
from flet import FilePicker
# from flet import FilePickerResultEvent

from src.filesystem.cli_star_ficha import star_ficha


def main(page: ft.Page):  
    #     1. Настройка "холста"
    page.title = "Анализатор" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='Путь',   hint_text='Введите путь к директории')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    hello_text = ft.Text(value = "Анализатор директории готов к работе\nРежим ожидания ввода пути к директории",  size=20, color="blue")
     # Создаем объект пикера
    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            print(text_path.value, 27)
            path = os.path.normpath(str(text_path.value))
            page.session.set('result', path)
            # return text_path.value
        else:
            # Если нажали отмену - не даем программе упасть [cite: 7, 8]
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!
    # page.controls.append(get_directory_dialog)
        
    # # Кнопка, которая открывает окно Windows
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.icons.FOLDER_OPEN,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" # Тот самый тултип!
    )  
    def on_button_click_1(e): 
        
        # 2. Обновляем текст
        hello_text.value = 'Нажмите кнопку\nЗапуск Анализатора'
        hello_text.color = "green"
                
        text_path.color = "yellow"
        #делаем невидимыми поле для ввода пути и кнопку Ввод
        text_path.visible = False
        btn1.visible = False
        # делаем видимым кнопку  Запуск Анализатора
        btn.visible = True
        page.update()
       
        path = os.path.normpath(str(text_path.value))
        page.session.set('result', path)
    
    btn1 = ft.ElevatedButton('ВВОД', icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_button_click_1)  

    result_container = ft.Column(
    width=600,         # Ширина области
    height=400,        # Высота области (настройте под свой экран)
    scroll=ft.ScrollMode.ALWAYS, # Всегда показывать полосу прокрутки
    controls=[]        # Сюда мы будем "подкладывать" наш текст
)

# 2. В функции анализа вместо hello_text.value делаем так:
    def on_button_click(e):
        try:
            res = page.session.get('result')
            fresh_result = star_ficha(res)
            # print(type(fresh_result), fresh_result, 68)
            res_list = fresh_result.split('\n')
            # print(res_list, 70)
            page.session.set('res_list', res_list)
            text_button.color = "yellow"
            # делаем видимой кнопку вывода в файл
            btn2.visible = True
            # Формируем надпись под выводимыми данными
            hello_text.value = "РЕЗУЛЬТАТ"
            hello_text.color = 'red'
            hello_text.size = 30
            # Очищаем контейнер перед новым выводом
            result_container.controls.clear()
            # Добавляем наш результат  в полосу прокрутки (теперь можно вернуть крупный шрифт!)
            
            result_container.controls.append(
                ft.Text(value=fresh_result, size=18, color="green", font_family="Consolas")
            )
            # Скрываем кнопку запуска
            btn.visible = False
        except Exception as err:
            result_container.controls.append(ft.Text(f"❌ Ошибка: {err}", color="red"))
        
        page.update()
    def on_button_click_2(e):
        hello_text.value = "✅ Отчет сохранен в report.scv!"
        import csv
        res_list = page.session.get('res_list')
        headers = ['РЕЗУЛЬТАТ']
        with open("report.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for line in res_list:
                writer.writerow([line])  # Оборачиваем строку в список

    def reset_app(e):
        
        # text_button.color = "red"
        hello_text.value = "Анализатор директории готов к работе\nРежим ожидания ввода пути к директории"
        hello_text.color = 'blue'
        page.session.set(None, None)
        text_path.color = "blue"
        text_path.value = None
        # возвращаем видимость кнопки и поля для ввода пути к директории
        text_path.visible = True
        btn1.visible = True
        # прячем кнопку вывода в файл
        btn2.visible = False
        # прячем строку "text_path.helper_text"
        text_path.helper_text = ''
        # удаляем содержимое окна прокрутки
        result_container.controls.clear()
        page.update()
        
         # Создаем кнопку с начальным стилем
    # button = ft.ElevatedButton(
    #     text="Нажми меня",
    #     style=ft.ButtonStyle(
    #         bgcolor=ft.colors.BLUE,
    #         text_style=ft.TextStyle(font_size=20, color=ft.colors.WHITE)
    #     )
    # )   
        
        
    text_button = ft.Text("Запуск Анализатора", size=25, color="red")  
      
    btn = ft.ElevatedButton("Запуск Анализатора",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_button_click)  
    # Собираем кнопку для  вывода результата в файл csv
    # text_button2 = ft.Text(text="Вывод Анализа в csv", size=25, color="red")     
    btn2 = ft.ElevatedButton("Вывод Анализа в csv", icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_button_click_2)  
    btn2.visible = False
    
    # делаем кнопку Запуск Анализатора изначально  невидимой
    btn.visible = False
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, on_click=reset_app)



# 3. Тот самый метод .add() с кортежем *controls
    page.add(text_path, ft.Row([btn1, btn_select], spacing=20),
            
        ft.Row([btn, btn2, btn_reset], alignment=ft.MainAxisAlignment.CENTER, spacing=20 ),
        ft.Row(
            [hello_text],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([result_container], alignment=ft.MainAxisAlignment.CENTER)

            ) 

ft.app(target=main)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    
    args = parser.parse_args()
    
    try:
     ft.app(target=main)
    except Exception as e:
        logging.error(e)

