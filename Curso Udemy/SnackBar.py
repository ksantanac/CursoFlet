import flet as ft

# flet -r SnackBar.py
def main(page: ft.Page):

    def show_sb(e):
        page.snack_bar.open = True
        page.update()

    # Mensagem de aviso
    page.snack_bar = ft.SnackBar(
        content= ft.Text(value="Não foi possivel processar os dados nesse momento."),
        bgcolor= ft.colors.RED_100,
        show_close_icon= True,
        close_icon_color= ft.colors.RED,
        padding= ft.padding.all(10),
        duration=10000,

        # Fixa em todo a tela, o FLOATING da uma margem
        behavior= ft.SnackBarBehavior.FLOATING,
        margin= ft.margin.all(50),

        # Fechar arrastando
        dismiss_direction= ft.DismissDirection.START_TO_END,

        # action= "Ok"
        # action_color=ft.colors.GREEN,
        # on_action= lambda _: print("Ação selecionada")
    )

    btn = ft.ElevatedButton(text="Abrir SnackBar", on_click=show_sb)

    page.add(btn)


if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)