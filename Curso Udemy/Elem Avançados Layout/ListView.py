# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r ListView.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.scroll = ft.ScrollMode.AUTO

    lv = ft.ListView(
        controls=[ft.Text(f"Item {i}") for i in range(101)],
        first_item_prototype= False,
        horizontal=False,
        # item_extent=40,
        padding=ft.padding.all(100),
        spacing=20,
        divider_thickness=3
    )

    page.add(lv)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
