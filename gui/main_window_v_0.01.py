import os

import flet as ft
from src.filesystem.cli_star_ficha import star_ficha


def main(page: ft.Page):
    page.title = "Анализатор Pro"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Создаем ОДИН объект для вывода текста
    status_text = ft.Text(value="Режим ожидания ввода пути", size=20, color="blue")

    # Поле ввода
    path_input = ft.TextField(label='Путь', hint_text='Введите путь к директории')

    # Функция анализа
    def start_analysis(e):
        if not path_input.value:
            status_text.value = "⚠️ Сначала введите путь!"
            status_text.color = "red"
            page.update()
            return

        try:
            # Напрямую берем значение из поля ввода!
            res = star_ficha(os.path.normpath(path_input.value))
            status_text.value = res
            status_text.color = "green"
        except Exception as err:
            status_text.value = f"❌ Ошибка: {err}"
            status_text.color = "red"
        page.update()

    # Функция сброса
    def reset_app(e):
        path_input.value = ""
        status_text.value = "Система сброшена. Жду путь."
        status_text.color = "blue"
        page.update()

    # Кнопки
    btn_run = ft.ElevatedButton("Запуск Анализа", icon=ft.Icons.PLAY_ARROW_SHARP, on_click=start_analysis)
    btn_reset = ft.ElevatedButton("Сброс", icon=ft.Icons.REFRESH, on_click=reset_app)

    # Собираем интерфейс (Layout) [cite: 185]
    page.add(
        path_input,
        ft.Row([btn_run, btn_reset], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(), # Визуальная черта
        status_text
    )
ft.app(target=main)
# if __name__ == "__main__":
#     ft.app(target=main)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Считаем размер папок и файлов на уровне вызова")
#     parser.add_argument("path", help="Путь к папке")

#     args = parser.parse_args()

#     try:
#        star_ficha(args.path)
#     except Exception as e:
#         logging.error(e)
