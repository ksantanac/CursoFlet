import flet as ft


# flet -r AppBar.py
def main(page: ft.Page):
    # page.bgcolor = ft.colors.WHITE
    def change_mode(e):

        e.control.selected = not e.control.selected

        if e.control.selected:
            page.bgcolor = ft.colors.WHITE
            page.update()
        else:
            page.bgcolor = ft.colors.BLACK
            page.update()

    def open_sb(e):
        aviso.open = True
        page.update()

    avatar = ft.CircleAvatar(
        col=2,
        foreground_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW4QHBQ1-BIWQT5YaT5fILo9_PVy-TJICgaA&usqp=CAU",
        # height=60,
        # width=60,
        content=ft.Column(
            controls=[
                ft.Icon(name=ft.icons.CHAT, col=1, color=ft.colors.BLACK),
            ]
        )
    )


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

    page.appbar = ft.AppBar(
        bgcolor=ft.colors.BLACK,
        title=ft.Text(value="App Fit"),
        center_title=False,
        toolbar_height=100,
        color=ft.colors.AMBER,
        leading=ft.Icon(name=ft.icons.HOME),
        leading_width=100,
        actions=[
            ft.Container(
                content=ft.IconButton(icon=ft.icons.SUNNY, on_click=change_mode),
                margin=ft.margin.symmetric(horizontal=10),
            ),
            ft.Container(
                content=ft.IconButton(icon=ft.icons.NOTIFICATIONS, on_click=open_sb),
                margin=ft.margin.symmetric(horizontal=10),
            ),
            ft.Container(
                avatar,
                margin=ft.margin.symmetric(horizontal=10),
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Meus dados"),
                    ft.PopupMenuItem(text="Configurações"),
                    ft.PopupMenuItem(text="Sair"),
                ]
            )

        ],

    )

    page.add(aviso)


if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)
