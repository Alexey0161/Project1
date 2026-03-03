import flet as ft


def main(page: ft.Page):
    username = ft.TextField(label="Username", hint_text="Enter your username")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    def btn_click(e):
        print(f"Logging in: {username.value}")

    page.add(username, password, ft.Button("Login", on_click=btn_click))


ft.run(main)