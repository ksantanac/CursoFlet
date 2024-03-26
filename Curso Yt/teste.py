from flet import *

def main(page: Page):
    page.add(
        Text("Ola mundo")
    )

# flet -r teste.py cmd

app(target=main)