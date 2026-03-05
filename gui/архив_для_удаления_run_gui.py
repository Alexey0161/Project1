import argparse
import flet as ft
import logging
from show_star_gui import star_gui

def main_show(page: ft.Page):
    
# 1. Настройка холста
    page.title = "Анализатор" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text(value = "Главное меню \nВыберите нужную кнопку",  size=20, color="blue")
    
    def open_star_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        star_gui(page) # Вызываем фичу графики Звездочки

        page.update()
    page.update()
    


    btn1 = ft.ElevatedButton("Запуск Анализатора",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_star_gui,
                            tooltip="Кнопка для запуска Анализа выбранной папки")  

    page.add(ft.Row([btn1], spacing=20),
            ft.Row(
            [hello_text],
            alignment=ft.MainAxisAlignment.CENTER
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