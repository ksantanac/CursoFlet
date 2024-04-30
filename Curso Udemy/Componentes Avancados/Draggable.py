import flet as ft


# flet -r Draggable.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):
    dg1 = ft.Row(
        controls=[
            ft.Draggable(
                group="color",
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.CYAN,
                    border_radius=5
                ),
                content_feedback=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.with_opacity(0.5, ft.colors.AMBER),
                    shape=ft.BoxShape.CIRCLE
                ),
                content_when_dragging=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.GREY_100
                )
            ),

            ft.Draggable(
                group="color",
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.AMBER,
                    border_radius=5
                )
            ),

            ft.Draggable(
                group="color",
                content=ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.colors.RED,
                    border_radius=5
                )
            ),

        ]
    )

    def drag_will_accept(e):
        e.control.content.border = ft.border.all(
            5, ft.colors.GREEN if e.data == "true" else ft.colors.RED
        )
        e.control.update()

    def drag_accept(e):
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None

        e.control.update()

    def drag_leave(e):
        e.control.contet.border = None
        e.control.update()

    target = ft.DragTarget(
        content=ft.Container(
            width=300,
            height=300,
            bgcolor=ft.colors.GREY_100,
        ),
        group="color",
        on_will_accept=drag_will_accept,
        on_accept=drag_accept,
        on_leave=drag_leave
    )

    page.add(dg1, target)


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
