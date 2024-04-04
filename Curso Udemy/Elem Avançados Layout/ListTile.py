# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r ListTile.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    lt1 = ft.ListTile(
        title=ft.Text(value="Titulo do primeiro"),
        subtitle=ft.Text(value="Subtitulo do primeiro"),
        leading=ft.Icon(ft.icons.ADB),
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Item 1"),
                ft.PopupMenuItem(text="Item 2")
            ]
        ),
        content_padding=ft.padding.all(20),
        selected=True,
        on_click=lambda _: print("Clicado"),
        url = "https://google.com",

    )

    lt2 = ft.ListTile(
        title=ft.Text(value="Titulo segundo"),
        leading= ft.Icon(name=ft.icons.ADB),
        trailing=ft.Switch(),
        toggle_inputs=True
    )

    page.add(lt1, lt2)


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
