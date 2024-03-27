import flet as ft


# flet -r NavigationRail.py
def main(page: ft.Page):

    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label="Inicio"
            ),
            ft.NavigationRailDestination(
                label="Chat"
            ),
            ft.NavigationRailDestination(
                icon= ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Itens salvos",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Container(bgcolor="red", height=20, width=20),
                selected_icon_content=ft.Container(bgcolor="green", width=20, height=20),
                label="Configurações",
                # label_content=ft.Text(value=""),
                padding=ft.padding.only(top=50),
            )
        ],

        bgcolor=ft.colors.GREY_900,
        selected_index=0,
        # Icone a esquerda e o label a direita
        extended=True,

        # Definir tamanho minimo
        # min_width=200,

        # Tamanho minimo da versao estendida
        min_extended_width=200,

        # Ao final da barra
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Cadastrar novo"),
                ft.PopupMenuItem(text="Enviar mensagem")
            ],

        ),

        # No começo da barra
        leading=ft.CircleAvatar(content=ft.Text(value="PA")),

        on_change= lambda e: print(e.control.selected_index)


    )

    row = ft.Row(controls=[rail], expand=True)

    page.add(row)


if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)
