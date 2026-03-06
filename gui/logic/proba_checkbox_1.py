import flet as ft
# ###########  Экспериментально для проверки возможносте добавляю ft.Checkbox
def main(page: ft.Page):
    # btn_recursive = ft.Checkbox('Рекурсия')
    recursive_mode = False
    page.session.set('recursive', recursive_mode)
    
    
    def on_checkbox_change(e):
        # nonlocal recursive_mode
        recursive_mode = page.session.get('recursive')
        recursive_mode = e.control.value
        if recursive_mode:
            print("Запуск с рекурсией")
            
        else:
            print("Запуск без рекурсии")
            
    
    btn_recursive = ft.Switch('Рекурсия', value=recursive_mode)
    btn_recursive.on_change = on_checkbox_change
    
        # добавляем элемент на страницу
    page.add(btn_recursive)

ft.app(target=main)