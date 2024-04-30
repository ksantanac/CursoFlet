import flet as ft

#flet -r Keyboard.py
def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):

        tecla = ""

        if e.ctrl:
            tecla += "Ctrl + "

        if e.shift:
            tecla += "Shift + "

        if e.alt:
            if page.platform == "macos":
                tecla = "Opt + "
            else:
                tecla += "Alt + "

        tecla += e.key
        page.add(ft.Text(value=tecla))


    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Aperte algum botão")
    )


if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)