import flet as ft


# flet -r ShakeDetector.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    t =  ft.Text(value="Aguardando...")
    def shake(e):
        t.value = ("Balanço detectado")
        t.update()
        
    shd = ft.ShakeDetector(
        minimum_shake_count=2,
        shake_slop_time_ms=200,
        shake_count_reset_time_ms=1000,
        on_shake=shake,
    )

    page.overlay.append(shd)
    page.update()

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
