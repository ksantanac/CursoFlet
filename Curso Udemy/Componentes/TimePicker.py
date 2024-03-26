import flet as ft
import datetime

# flet -r TimePicker.py
def main(page: ft.Page):

    tp = ft.TimePicker(
        cancel_text="Cancelar",
        confirm_text="Confirmar",
        error_invalid_text="Hora inválida",
        hour_label_text="Hora",
        minute_label_text="Minutos",
        help_text="Selecione a hora",
        time_picker_entry_mode=ft.TimePickerEntryMode.INPUT,
        # value = datetime.time(22, 31, 18)

        on_change=lambda _: print(tp.value)
    )

    page.overlay.append(tp)

    btn = ft.ElevatedButton("Abrir", on_click= lambda _: tp.pick_time())
    page.add(btn)

if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)