import flet as ft
import datetime

# flet -r DatePicker.py
def main(page: ft.Page):

    dp = ft.DatePicker(

        cancel_text= "Cancelar",
        confirm_text= "Confirmar",
        error_format_text= "Data inválida",
        field_hint_text= "DD/MM/YYYY",
        field_label_text= "Digite uma Data",
        help_text= "Selecione uma data",
        switch_to_calendar_icon= ft.icons.CALENDAR_MONTH,
        switch_to_input_icon= ft.icons.EDIT,

        date_picker_mode= ft.DatePickerMode.DAY,
        date_picker_entry_mode= ft.DatePickerEntryMode.CALENDAR,

        # Se quiser abrir direto numa data
        value= datetime.date(2024, 1, 10),

        # Limitar datas
        first_date=datetime.date(2024, 1, 5),
        last_date=datetime.date(2024, 1, 20),

        error_invalid_text="Data indisponivel",

        # Pegar a data selecionada
        on_change=lambda _: print(dp.value),

        # Selecionar qual tipo de teclado será aberto
        keyboard_type=ft.KeyboardType.NUMBER

    )

    page.overlay.append(dp)
    btn = ft.ElevatedButton("Abrir", on_click= lambda _: dp.pick_date()) # PickDATE para abrir o calendario

    page.add(btn)


if __name__ == '__main__':
    # Open the webpage and run the function on it
    ft.app(target=main)