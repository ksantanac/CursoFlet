# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r DataTable.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):
    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f"Selecionando a linha de índice {e.control.data}")
        e.control.update()


    dt = ft.DataTable(
        columns=[

            ft.DataColumn(label=ft.Text("Nome", color=ft.colors.BLACK)),
            ft.DataColumn(label=ft.Text("Login"), tooltip="Login do usuário na plataforma"
                          ),
            ft.DataColumn(
                label=ft.Text("Idade"),
                numeric=True,
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),

            ),
        ],
        rows=[
            ft.DataRow(


                cells=[
                    # ft.Row(
                    #     controls=[
                    #         ft.Text("Maria", color=ft.colors.BLUE),
                    #         ft.Icon(name=ft.icons.EDIT),
                    #     ]
                    # ),

                    ft.DataCell(
                        content=ft.Row(
                            controls=[
                                ft.Text("Maria", color=ft.colors.BLACK),
                                ft.Icon(name=ft.icons.EDIT, color=ft.colors.WHITE),
                            ]
                        ),
                        # content=ft.Text("Maria"),
                        # show_edit_icon=True,
                        on_tap=lambda _: print("Clicada"),
                    ),
                    ft.DataCell(content=ft.Text("mary99")),
                    ft.DataCell(content=ft.Text("43")),
                ],
                selected=False,
                on_select_changed=toggle_select,
                data= 0,

            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text("João")),
                    ft.DataCell(content=ft.Text("joao33")),
                    ft.DataCell(content=ft.Text("19")),
                ],
                selected=False,
                on_select_changed=toggle_select,
                data=1
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(content=ft.Text("Kaue")),
                    ft.DataCell(content=ft.Text("kaue33")),
                    ft.DataCell(content=ft.Text("20")),
                ],
                selected=False,
                on_select_changed=toggle_select,
                data=2
            ),
        ],
        show_checkbox_column=True,
        bgcolor=ft.colors.GREY_900,
        border=ft.border.all(width=2, color=ft.colors.BLACK),
        border_radius=ft.border_radius.all(5),
        column_spacing=100,
        data_row_min_height=10,
        data_row_max_height=50,
        data_text_style=ft.TextStyle(italic=True),
        divider_thickness=1,
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.center_left,
        #     end=ft.alignment.center_right,
        #     colors=[ft.colors.TEAL, ft.colors.CYAN],
        # ),
        data_row_color={
            ft.MaterialState.SELECTED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.GREY_700,
        },
        heading_row_color=ft.colors.BLACK,
        heading_row_height=50,
        heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        # horizontal_lines=ft.BorderSide(width=5, color=ft.colors.AMBER),
        # horizontal_lines=ft.BorderSide(width=1, color=ft.colors.GREEN),
        horizontal_margin=50,
        show_bottom_border=True,
        sort_column_index=2,
        sort_ascending=True,

    )

    page.add(dt)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
