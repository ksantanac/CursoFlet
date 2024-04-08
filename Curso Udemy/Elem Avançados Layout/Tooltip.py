# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Tooltip.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    ...

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
