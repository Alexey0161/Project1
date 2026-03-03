import flet as ft
 
# ft.FilePicker
print(dir(ft))


def main(page: ft.Page):  
    # Создаем объект пикера
    
    text_path = ft.TextField(label='Путь',   hint_text='Введите путь к директории')
    


    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.path:
            # Если путь выбран - обновляем поле и радуем пользователя
            text_path.value = e.path
            text_path.helper_text = "✅ Путь успешно выбран"
            text_path.helper_style = ft.TextStyle(color="green")
            return text_path.value
        else:
            # Если нажали отмену - не даем программе упасть [cite: 7, 8]
            text_path.helper_text = "⚠️ Выбор отменен"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(get_directory_dialog) # Обязательно добавляем на холст!
        
    # # Кнопка, которая открывает окно Windows
    btn_select = ft.ElevatedButton(
        "Выбрать папку",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: get_directory_dialog.get_directory_path(),
        tooltip="Нажмите, чтобы выбрать папку через проводник Windows" # Тот самый тултип!
    )    