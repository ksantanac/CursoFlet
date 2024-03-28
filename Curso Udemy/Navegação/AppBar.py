# Importe a biblioteca flet com o alias ft
import flet as ft

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):
    # Defina uma função para alternar entre os modos de cor de fundo da página
    def change_mode(e):
        e.control.selected = not e.control.selected

        # Alterna entre as cores de fundo da página dependendo do modo selecionado
        if e.control.selected:
            page.bgcolor = ft.colors.WHITE
            page.update()
        else:
            page.bgcolor = ft.colors.BLACK
            page.update()

    # Defina uma função para abrir a Snackbar (barra de notificação)
    def open_sb(e):
        aviso.open = True
        page.update()

    # Crie um avatar circular com um ícone de chat
    avatar = ft.CircleAvatar(
        col=2,
        foreground_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW4QHBQ1-BIWQT5YaT5fILo9_PVy-TJICgaA&usqp=CAU",
        content=ft.Column(
            controls=[
                ft.Icon(name=ft.icons.CHAT, col=1, color=ft.colors.BLACK),
            ]
        )
    )

    # Crie uma Snackbar para exibir notificações
    aviso = ft.SnackBar(
        content=ft.Text("Você não tem nenhuma notificação", color=ft.colors.BLACK, size=16),
        bgcolor="#E9F5FE",
        show_close_icon=True,
        close_icon_color=ft.colors.BLACK,
        padding=ft.padding.all(10),
        duration=5000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.margin.all(50),
        dismiss_direction=ft.DismissDirection.START_TO_END,
    )

    # Configure a AppBar (barra de aplicativo) com diferentes elementos
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.BLACK,  # Cor de fundo da barra de aplicativo
        title=ft.Text(value="App Fit"),  # Título da barra de aplicativo
        center_title=False,  # Alinhamento do título
        toolbar_height=100,  # Altura da barra de ferramentas
        color=ft.colors.AMBER,  # Cor de destaque
        leading=ft.Icon(name=ft.icons.HOME),  # Ícone à esquerda
        leading_width=100,  # Largura do ícone à esquerda
        actions=[  # Ações à direita da barra de aplicativo
            # Botão para alternar entre modos de cor de fundo
            ft.Container(
                content=ft.IconButton(icon=ft.icons.SUNNY, on_click=change_mode),
                margin=ft.margin.symmetric(horizontal=10),
            ),
            # Botão para abrir a Snackbar
            ft.Container(
                content=ft.IconButton(icon=ft.icons.NOTIFICATIONS, on_click=open_sb),
                margin=ft.margin.symmetric(horizontal=10),
            ),
            # Avatar circular
            ft.Container(
                avatar,
                margin=ft.margin.symmetric(horizontal=10),
            ),
            # Botão de menu suspenso com itens de menu
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Meus dados"),
                    ft.PopupMenuItem(text="Configurações"),
                    ft.PopupMenuItem(text="Sair"),
                ]
            )
        ],
    )

    # Adicione a Snackbar à página
    page.add(aviso)

# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
