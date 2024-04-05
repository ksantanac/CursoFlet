# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Dismissible.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.scroll = ft.ScrollMode.AUTO
    def handle_dismiss(e):
        lv.controls.remove(e.control)
        lv.update()

    lv = ft. ListView(
        controls=[

            ft.Dismissible(
                content=ft.Text(value=f"Item {i}", size=40),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.YELLOW, content=ft.Text(value="Arquivar", color=ft.colors.BLACK)),
                secondary_background=ft.Container(bgcolor=ft.colors.RED, content=ft.Text(value="Excluir")),
                on_dismiss=handle_dismiss,
                on_update=lambda _: print("Atualizado"),
                on_resize=lambda _: print("Redimensionado")
            ) for i in range(30)
        ]
    )

    page.add(lv)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
