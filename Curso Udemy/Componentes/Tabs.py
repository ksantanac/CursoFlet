import flet as ft
import datetime

# flet -r Tabs.py
def main(page: ft.Page):

    t = ft.Tabs(
        tabs = [
            ft.Tab(
                text="Tab 1",
                content= ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Text("Conteudo da TAB 1")
                )
            ),

            ft.Tab(
                icon=ft.icons.SETTINGS,
                content=ft.Text("Conteudo da TAB 2")
            ),
            # ft.Tab(
            #     tab_content= ft.Container(
            #         content= ft.Badge(
            #             bgcolor=ft.colors.GREEN,
            #             content=ft.CircleAvatar(
            #                 foreground_image_url="https://avatars.gitubusercontent.com/u/144709944?s=200&v=4",
            #                 tooltip="Programdor Aventureiro"
            #             ),
            #             small_size=10,
            #         ),
            #     ),
            # )
        ],
        # Qual TAB vai abrir
        selected_index=1,
        animation_duration=300,
        divider_color=ft.colors.AMBER,
        indicator_border_radius=ft.border_radius.all(10),
        indicator_color=ft.colors.RED,
        indicator_padding=ft.padding.all(5),
        indicator_tab_size=True,
        label_color=ft.colors.GREEN,
        unselected_label_color=ft.colors.WHITE,

        overlay_color= {
            ft.MaterialState.HOVERED: ft.colors.GREY
        },

        # scrollable=False
    )

    page.add(t)


if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)