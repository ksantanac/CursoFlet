import flet as ft

def main(page: ft.Page):

    page.window_width = 500
    page.window_height = 550

    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.RED,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color="black", size=40),
        content=ft.Text("Preencha todos os campos!", color="black"),
        actions=[
            ft.TextButton("Ok", on_click=close_banner)
        ]
    )

    # Função adicionar tarefa
    def adicionar(e):

        if nova_tarefa.value == "":
            page.banner.open = True
            page.update()
        else:
            page.add(ft.Checkbox(label= nova_tarefa.value))
            nova_tarefa.value = ""
            nova_tarefa.focus()
            nova_tarefa.update()


    nova_tarefa = ft.TextField(hint_text="Adicione sua tarefa", width=300)

    botao_add = ft.ElevatedButton(text="Adicionar", on_click=adicionar)

    page.add(ft.Row([nova_tarefa, botao_add]))


ft.app(target=main)