import argparse
import flet as ft 
import os
import logging
from src.filesystem.cli_modif_files import process_logic



def modif_gui(page: ft.Page):  
    
# 1. Настройка "холста"
    page.title = "Модификатор" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    
    text_path = ft.TextField(label='ВЫБЕРИТЕ папку через Проводник через кнопку "ВЫБРАТЬ ПАПКУ"',   hint_text='Путь')
    text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
    hello_text = ft.Text(value = "Модификатор имени файла готов к работе\nРежим ожидания ввода имени файла",  size=20, color="blue")
 
## 2. Задаем  функции кнопок:

### 2.1. Задаем функцию Выбора папки 
    def on_dialog_result(e):  # Выбор из Windows
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "                     Путь выбран ----> Выберите режим:\n- с рекурсией: ползунок передвиньте вправо\n- без рекурсии: оставьте ползунок в исходном положении"
            hello_text.color = "red"
            hello_text.size = 30
            path = os.path.normpath(str(text_path.value))
            page.session.set('directory', path)
            # убираем кнопку выбора из windows
            btn_select.visible = False
            # делаем видимыми кнопки выбора режима Рекурсии:
            btn_confirm.visible = True
            # делаем видимым Ползунок выбора режима Рекурсии
            btn_switch.visible = True
            # делаем видимой кнопку Сброс
            btn_reset.visible = True
            
        else:
            # Если нажали отмену - не даем программе упасть 
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!

## 2.2. Функции выбора режима Ползунка "Рекурсия" и кнопки подтверждения режиа "Старт"
    # 2.2.2. Функция Ползунка выбора режиа РЕКУРСИЯ:
    page.session.set('recursive', False)

    def on_switch_change(e): # Ползунок Рекурсия
        # Просто сохраняем новое значение напрямую в сессию
        page.session.set('recursive', e.control.value)
        btn_confirm.visible = True
        page.update()

    # 2.2.3. Создаем функцию  Кнопки "Подтвердить Выбор" подтверждения выбора режима Рекурсия или без него
    def on_button_confirm(e):
        # Достаем значение из сессии прямо в момент клика
        is_recursive = page.session.get('recursive')
        path = page.session.get('directory')
        
        if is_recursive:
            path_with_rec = (path, 'recursive')
            page.session.set('path', path_with_rec)
            # Делаем информационное сообщение
            hello_text.value = "       Подтвержден режим с рекурсией\nНажмите кнопку Запуск Модификатора"
            hello_text.color = 'green'
            # убираем строку выбора из windows
            text_path.visible = False
            # убираем кнопку Подтвердить Выбор
            btn_confirm.visible = False
            # убираем Ползунок выбора режима Рекурсии
            btn_switch.visible = False
            # Открываем Кнопку Запуск Модификатора
            btn_modif.visible = True
            print("🚀 Запуск С РЕКУРСИЕЙ", path_with_rec)
        else:
            path_out_rec = (path,)
            page.session.set('path', path_out_rec)
            # Делаем информационное сообщение
            hello_text.value = "       Подтвержден режим БЕЗ рекурсией\nНажмите кнопку Запуск Модификатора"
            hello_text.color = 'green'
            # убираем строку выбора из windows
            text_path.visible = False
            # убираем кнопку Подтвердить выбор
            btn_confirm.visible = False
            # убираем Ползунок выбора режима Рекурсии
            btn_switch.visible = False
            # Открываем Кнопку Запуск Модификатора
            btn_modif.visible = True
            print("🎯 Запуск БЕЗ РЕКУРСИИ", path_out_rec)
            
        btn_confirm.visible = False
        page.update()
  
### 2.3. Создаем функцию кнопки Запуск Модификатора
    def on_button_modif(e): # Запуск Анализатора
        try:
            # забираем из page.session путь записанный в функции on_button_click_1
            res = page.session.get('path')
            
            # запускаем функцию process_logic, которую мы импортировали из cli_star_ficha
            process_logic(*res)
            # Убираем кнопку Запуск Модификатора
            btn_modif.visible = False
            # Выводим информацию об успешном завершении программы
            hello_text.value = "В имена файлов добавлены даты"
        except Exception as err:
            text_mistake = ft.Text(f"❌ Ошибка: {err}", color="red"
                                   ,  size = 30)
        page.update()
### 2.4. Собираем функцию кнопки Сброс
    def reset_app(e): # Сброс
        
        text_path.value = None
        btn_select.visible = True
        text_path.visible = True # на стартовом окне поле для ввода пути делаем видимым
        hello_text.value = "Модификатор имени файла готов к работе\nРежим ожидания ввода имени файла"
        page.session.set(None, None)
        text_path.color = "blue"
        # убираем помощь
        text_path.helper_text = ''
        #  убираем кнопку Сброс
        btn_reset.visible = False
       
        page.update()
###  2.5. Собираем функцию Кнопки Домой 
    def on_home(e):
        from run_gui import main_show
        page.clean() # очищаем экран от элементов графики Звездочки
        main_show(page) # вызываем Главное Меню/Единое окно
        page.update()     
    page.update()

## 3.              РАЗДЕЛ  - задание ВСЕХ кнопок  
    ### 3.1. Задание Кнопки выбора файла из проводника  Windows (функция on_dialog_result)
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.icons.FOLDER_OPEN,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" #  тултип
    )  

    ### 3.2. Создаем Ползунок Режима выбора Рекурсии
    btn_switch = ft.Switch(label='Рекурсия', value=False,visible=False, on_change=on_switch_change, 
                           tooltip='Выбрать режим с Рекурсией или без')
    ### 3.3. Создаем кнопку подтверждения выбранного Режима Рекурсии
    btn_confirm = ft.ElevatedButton(text='Подтвердить Выбор', visible=False, disabled=False, on_click = on_button_confirm,
                            tooltip='Подтвердить выбранный режим Рекурсии')
    ### 3.4. Задаение Кнопки "Запуска Модификатора"
    btn_modif = ft.ElevatedButton(
        "Запустить Модификатор",
        icon=ft.icons.PLAY_ARROW_SHARP, visible=False,
        on_click=on_button_modif,
        tooltip="Нажмите, чтобы запустить Модификатор файлов" #  тултип
                                )  
    ### 3.5. Задание Кнопки Сброс
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.icons.REFRESH, visible = False, on_click=reset_app,
                                  tooltip="Кнопка для сброса и перевода окна в готовность к работе")

    ### 3.6.  Собираем Кнопку Домой     
    btn_home = ft.ElevatedButton("ДОМОЙ", icon=ft.icons.PLAY_ARROW_SHARP, on_click=on_home,
        tooltip="Нажмите, чтобы перейти в Главное меню выбора фичей") #  тултип


### 4. Добавляем элементы графики на страницу Окна -  метод .add() с кортежем *controls
    # page.add(text_path, ft.Container(content=ft.Column([btn_switch, btn_confirm, btn_modif, btn_reset], spacing=20, 
    #                                  alignment=ft.MainAxisAlignment.START),
    #          padding=ft.padding.only(left=20, top=40)
    #                                  ),
    #           ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER),
    #           ft.Row([btn_select], spacing=20),
    #                ft.Container(
    #     content=ft.Row([btn_home], alignment=ft.MainAxisAlignment.END),
    #     padding=ft.padding.only(right=20, bottom=1) #  "подъемник" на 20 пикселей от края
    # )
    #          )
# Заменяем ваш текущий page.add на этот вариант:
    page.add(
        ft.Column(
            [
                text_path,
                ft.Row([btn_select], spacing=20),
                ft.Container(
                    content=ft.Column([btn_switch, btn_confirm, btn_modif, btn_reset], spacing=10),
                    padding=ft.padding.only(left=20, top=20)
                ),
                ft.Row([hello_text], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Spacer(), # <--- МАГИЯ ЗДЕСЬ: этот элемент "расталкивает" контент
                ft.Container(expand=True),
                ft.Container(
                    content=ft.Row([btn_home], alignment=ft.MainAxisAlignment.END),
                    padding=ft.padding.only(right=20, bottom=20)
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
     ft.app(target=modif_gui)
    except Exception as e:
        logging.error(e)
