import flet as ft

# flet -r aula.py
def main(page: ft.Page):

    def close_banner(e):
        page.banner.open = False
        page.update()

    def open_banner(e):
        page.banner = bn1
        bn1.open = True
        page.update()


    bn1 = ft.Banner(
        actions=[
            ft.TextButton(text="Cancelar", style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_banner),
            ft.TextButton(text="Tentar novamente", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
                          on_click=close_banner),
        ],
        content= ft.Text(value="Ops, parece que não conseguimos processar sua solitação no momento"),
        content_padding= ft.padding.all(20),
        leading=ft.Icon(name=ft.icons.WARNING_AMBER),

        # Forçar os botões "Actions" ficar na parte de baixo do banner
        force_actions_below= True,

        bgcolor=ft.colors.BLACK
    )

    btn = ft.ElevatedButton(text="Abrir", on_click=open_banner)

    page.add(btn)



if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)