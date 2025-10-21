import flet as ft 

def main(page: ft.Page):
    page.title = "Chat con IA - Parte 1"
    page.bgcolor = ft.Colors.GREY_100

    mensajes = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
    prompt = ft.TextField(label="Escribe tu mensaje...", expand=True)

    def burbuja(texto, es_usuario):
        return ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        texto,
                        color=ft.Colors.WHITE if es_usuario else ft.Colors.BLACK,
                        size=15,
                        selectable=True,
                    ),
                    bgcolor=ft.Colors.BLUE_400 if es_usuario else ft.Colors.GREY_300,
                    padding=12,
                    border_radius=30,
                    width=350,
                )
            ],
            alignment=ft.MainAxisAlignment.END if es_usuario else ft.MainAxisAlignment.START,
        )

    def enviar_click(e):
        texto = prompt.value.strip()
        if not texto:
            return
        mensajes.controls.append(burbuja(texto, True))
        prompt.value = ""
        # Simulated bot response
        mensajes.controls.append(burbuja("Hola, soy un bot simulado. ¡Parte 1 lista!", False))
        page.update()

    def limpiar_chat(e):
        mensajes.controls.clear()
        page.update()

    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar_click)
    prompt.on_submit = enviar_click

    page.add(
        ft.Column([
            ft.Row([ft.TextButton("🧹 Limpiar chat", on_click=limpiar_chat)], alignment=ft.MainAxisAlignment.START),
            mensajes,
            ft.Row([prompt, boton_enviar], vertical_alignment=ft.CrossAxisAlignment.END),
        ], expand=True)
    )
ft.app(target=main)
