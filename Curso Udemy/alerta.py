import flet as ft 

# flet -r aula.py
def main(page: ft.Page):

    def close_ad(e):
        print("Fechei")
        ad1.open = False
        page.update()
    
    def save_ad(e):
        print("Salvo")
        ad1.open = False
        page.update()

    ad1 = ft.AlertDialog(
        title= ft.Text(value="Aviso importante"),
        content = ft.Text(value = 'Você está prestes a deletar o dados da seção. Quer mesmo seguir?'),

        # Espaçamento das bordas para o conteudo interno
        content_padding= ft.padding.all(30),

        # Espaçamento externo da página
        inset_padding=ft.padding.all(10),

        # Se estiver "False" e clicar fora o alert sai
        modal= False,

        # Alterar formato do alerta
        shape = ft.RoundedRectangleBorder(radius=5),

        # Função disparada quando o alerta fechar
        # on_dismiss= lambda _: print("Fechei"),

        # Lista de componentes das ações pro usuario executar
        actions=[
            ft.TextButton(text="Cancelar", style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_ad),
            ft.ElevatedButton(text="Salvar", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
                              on_click=save_ad)
        ],
        # Posição dos botões
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_ad(e):
        page.dialog = ad1
        ad1.open = True
        page.update()

    btn1 = ft.ElevatedButton(text="Abrir", on_click=open_ad)

    page.add(btn1)

if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)