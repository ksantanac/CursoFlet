import flet as ft

# flet -r aula.py
def main(page: ft.Page):

    def show_bs(e):
        bs.open = True
        page.update()

    def close_Bs(e):
        bs.open = False
        page.update()

    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(value="Título", style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value="Conteudo do BottomSheet", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text="Fechar", on_click=close_Bs)
                ]
            ),
            padding=20,
        ),
        # Não fecha mais o bottomsheet
        dismissible= False,

        # Possibilita clicar e arrastar na posição vertical
        enable_drag= True,

        # Habilitar o scrool
        is_scroll_controlled=False,

        # Adiciona espaçamento para o texto nao ficar colado
        maintain_bottom_view_insets_padding= True,

        # Mostra o componente indicativo visual par aarrastar
        show_drag_handle= True
    )

    # sobreposição visual, permitindo que o usuário interaja com ele sem afetar o conteúdo principal da página
    page.overlay.append(bs)

    btn = ft.ElevatedButton(text="Abrir", on_click=show_bs)

    page.add(btn)

if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)