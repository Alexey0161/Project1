import argparse
import flet as ft
import logging
from gui.show_star_gui import star_gui

def main_show(page: ft.Page):
    
# 1. Настройка холста
    page.title = "Анализатор" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text(value = "Главное меню \nВыберите нужную кнопку",  size=20, color="blue")

## 2. Собираем функции кнопок запуска фичей
### 2.1. Собираем фичу кнопки запуска Звездочки    
    def open_star_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        star_gui(page) # Вызываем фичу графики Звездочки

        page.update()
    page.update()
    

## 3. Собираем кнопки запуска фичей
### 3.1. Собираем кнопку запуск фичи Звездочка
    btn_star = ft.ElevatedButton("Запуск Анализатора",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_star_gui,
                            tooltip="Кнопка для запуска Анализа выбранной папки")  

## 4. Собираем визуализацию элементов Единого окна
    page.add(#ft.Row([btn1], spacing=20),
            ft.Row(
            [hello_text],
            alignment=ft.MainAxisAlignment.CENTER
                   ),
            ft.Container(
        content=ft.Row([btn_star], alignment=ft.MainAxisAlignment.START),
        padding=ft.padding.only(left=20, top=40)
                        )
   

            )

####  Вызов функции 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
    
    args = parser.parse_args()
    
    try:
     ft.app(target=main_show)
    except Exception as e:
        logging.error(e)