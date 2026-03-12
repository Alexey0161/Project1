import argparse
import flet as ft
import logging
from gui.show_analize_gui import analize_gui
from gui.show_star_gui import star_gui
from gui.show_modif_gui import modif_gui
from gui.show_find_gui import find_gui
from gui.show_count_gui import count_gui 
from gui.show_delete_gui import delete_gui
from gui.show_copy_gui import copy_gui

def main_show(page: ft.Page):
        
# 1. Настройка холста
    page.title = "ГЛАВНОЕ МЕНЮ/ЕДИНОЕ ОКНО" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text(value = "      Главное меню \nВыберите нужную кнопку",  size=40, color="orange")

## 2. Собираем функции кнопок запуска фичей
### 2.1. Собираем фичу кнопки запуска Звездочки    
    def open_star_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        star_gui(page) # Вызываем фичу графики Звездочки

        page.update()
### 2.2. Собираем фичу кнопки запуска Анализа директорий
    def open_analize_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        analize_gui(page) # Вызываем фичу графики
        page.update()

### 2.3. Собираем фичу кнопки запуска Модификатора файлов
    def open_modif_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        modif_gui(page) # Вызываем фичу графики
        page.update()


### 2.4. Собираем фичу кнопки запуска Поисковика файлов        
    def open_find_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        find_gui(page) # Вызываем фичу графики
        page.update()
### 2.5. Собираем фичу кнопки запуска Счетчика файлов        
    def open_count_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        count_gui(page) # Вызываем фичу графики
        page.update()                
    page.update()
### 2.6. Собираем фичу кнопки запуска Удалитея  папок        
    def open_delete_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        delete_gui(page) # Вызываем фичу графики
        page.update()                
    page.update()
### 2.7. Собираем фичу кнопки запуска Копирователя файлов       
    def open_copy_gui(e):
        page.clean() # очищаем окно от элементов Главного меню
        copy_gui(page) # Вызываем фичу графики
        page.update()                
    page.update()
    

## 3. Собираем кнопки запуска фичей
### 3.1. Собираем кнопку запуска графики фичи Звездочка
    btn_star = ft.ElevatedButton("Запуск Звездного анализатора",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_star_gui,
                            tooltip="Кнопка для запуска Звездного Анализа выбранной папки")  
### 3.2. Собираем кнопку запуска графики фичи Анализ директорий    
    btn_analize = ft.ElevatedButton("Запуск Анализатора",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_analize_gui,
                            tooltip="Кнопка для запуска Анализа выбранной папки")
### 3.3. Собираем кнопку запуска графики фичи  Модификатор файлов
    btn_modif = ft.ElevatedButton("Запуск Модификатора имени файлов",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_modif_gui,
                            tooltip="Кнопка для запуска Модификатора имени файлов в  выбранной папке")  
### 3.4. Собираем кнопку запуска графики фичи  Поисковик файлов
    btn_find = ft.ElevatedButton("Запуск Поисковик  файлов меньше предельного размера",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_find_gui,
                            tooltip="Кнопка для запуска поисковика  файлов меньше предельного размера в  выбранной папке")      
### 3.5. Собираем кнопку запуска графики фичи  Счетчик файлов
    btn_count = ft.ElevatedButton("Запуск Счетчика  файлов в папке, включая вложенные папки",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_count_gui,
                            tooltip="Кнопка для запуска Счетичика  файлов в папке")      
### 3.6. Собираем кнопку запуска графики фичи  Счетчик файлов
    btn_delete = ft.ElevatedButton("Запуск Удалителя   папок",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_delete_gui,
                            tooltip="Кнопка для запуска Удалителя папок")      
### 3.7. Собираем кнопку запуска графики фичи  Счетчик файлов
    btn_copy = ft.ElevatedButton("Запуск Копирователя файлов",  icon=ft.icons.PLAY_ARROW_SHARP, on_click=open_copy_gui,
                            tooltip="Кнопка для запуска Копирователя файлов")      

## 4. Собираем визуализацию элементов Единого окна
    page.add(
            ft.Row(
            [hello_text],
            alignment=ft.MainAxisAlignment.CENTER
                   ),
            ft.Container(
        content=ft.Column([btn_star, btn_analize, btn_modif, btn_find, btn_count, btn_delete, btn_copy], spacing=20, alignment=ft.MainAxisAlignment.START),
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