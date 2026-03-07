  ### 2.1.  Создаем функцию Кнопки btn_select выбора папки из Windows   

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files:  # Проверяем, выбраны ли файлы
            selected_files = e.files
            first_file = selected_files[0]
            file_path = first_file.path

            text_path.value = file_path
            text_path.helper_text = "✅ Папка успешно выбрана"
            text_path.helper_style = ft.TextStyle(color="green")
            hello_text.value = "     Папка выбран\nНажмите кнопку ВВОД"
            hello_text.color = "red"
            hello_text.size = 30

            path = os.path.normpath(file_path)
            page.session.set('result', path)
        else:
            # Если нажали отмену или не выбрали файл
            text_path.helper_text = "⚠️ Выбор отменён"
            text_path.helper_style = ft.TextStyle(color="yellow")
        page.update()

    # Создаём FilePicker с обработчиком результата
    get_file_dialog = ft.FilePicker(on_result=on_dialog_result)
    # Добавляем FilePicker в оверлей страницы
    page.overlay.append(get_file_dialog)
