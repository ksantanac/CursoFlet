# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Views.py -w

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    def route_change(route):

        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text("Meu App"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                controls=[
                    ft.ElevatedButton(
                        text="Ver loja",
                        on_click=lambda _: page.go("/loja")
                    ),
                    ft.ListView(
                        controls=[
                            ft.Text(
                                value=f"Item {i}",
                                size=30
                            )
                            for i in range(50)
                        ]
                    )
                ],
                scroll=ft.ScrollMode.AUTO
            )
        )

        if page.route == "/loja":
            page.views.append(
                ft.View(
                    route= "/loja",
                    appbar=ft.AppBar(
                        title=ft.Text("Loja"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para página inicial",
                            on_click=lambda _: page.go("/")
                        ),
                        ft.ElevatedButton(
                            text="Ir para página App",
                            on_click=lambda _: page.go("/app")
                        )
                    ]
                )
            )

            if page.route == "/app":
                page.views.append(
                    ft.View(
                        route="/app",
                        appbar=ft.AppBar(
                            title=ft.Text("App"),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        controls=[
                            ft.ElevatedButton(
                                text="Ir para página inicial",
                                on_click=lambda _: page.go("/")
                            )
                        ]
                    )
                )


    def view_pop(view):
        # Retirar a ultima view
        page.views.pop()

        # Trocar a view
        top_view = page.views[-1]

        page.go((top_view.route))
    #
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
