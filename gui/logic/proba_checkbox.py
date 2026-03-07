import flet as ft

def main(page: ft.Page):
    # Инициализируем состояние в сессии при старте
    page.session.set('recursive', False)

    # 1. Обработчик Switch
    def on_switch_change(e):
        # Просто сохраняем новое значение напрямую в сессию
        page.session.set('recursive', e.control.value)
        btn_start.disabled = False
        page.update()

    # 2. Создаем элементы
    switch = ft.Switch(label='Рекурсия', value=False, on_change=on_switch_change)
    btn_start = ft.ElevatedButton(text='Запустить', disabled=False)

    # 3. Обработчик Кнопки
    def on_button_click(e):
        # Достаем значение из сессии прямо в момент клика
        is_recursive = page.session.get('recursive')
        
        if is_recursive:
            print("🚀 Запуск С РЕКУРСИЕЙ")
        else:
            print("🎯 Запуск БЕЗ РЕКУРСИИ")
            
        btn_start.disabled = True
        page.update()

    btn_start.on_click = on_button_click
    page.add(switch, btn_start)

ft.app(target=main)