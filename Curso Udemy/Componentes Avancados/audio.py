import flet as ft

# flet -r audio.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    def volume_down(e):
        audio.volume -= 0.1
        page.update()

    def volume_up(e):
        audio.volume += 0.1
        page.update()

    def balance_left(e):
        audio.balance -= 0.1
        page.update()

    def balance_right(e):
        audio.balance += 0.1
        page.update()




    audio = ft.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3",
        autoplay=False,
        balance=0, # 0 --> Som tocado nos canais | -1 --> tocado apenas lado esquerdo | 1 --> apenas lado direito
        volume=0.5,
        on_loaded=lambda _: print("carregado"),
        on_duration_changed=lambda e: print("Duração", e.data),
        on_position_changed=lambda e: print("Posição", e.data),
        on_state_changed=lambda e: print("Estado", e.data),
        on_seek_complete=lambda _: print("Completo"),
    )

    page.overlay.append(audio)

    t = ft.Text(value="Voluma: " + str(audio.volume))

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.PLAY_CIRCLE, on_click=lambda _: audio.play()),
                ft.IconButton(icon=ft.icons.PAUSE_CIRCLE, on_click=lambda _: audio.pause()),
                ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda _: audio.resume()),
                ft.IconButton(icon=ft.icons.FORWARD_10, on_click=lambda _: audio.seek(audio.get_current_position() + 10000)),
                ft.IconButton(icon=ft.icons.REPLAY_10, on_click=lambda _: audio.seek(audio.get_current_position() - 10000)),
            ]
        ),

        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.VOLUME_DOWN, on_click=volume_down),
                ft.IconButton(icon=ft.icons.VOLUME_UP, on_click=volume_up),
                ft.IconButton(icon=ft.icons.EXPOSURE_MINUS_1, on_click=balance_left),
                ft.IconButton(icon=ft.icons.EXPOSURE_PLUS_1, on_click=balance_right),
            ]
        ),
    )

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
