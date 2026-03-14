import flet as ft

def main(page: ft.Page):
    page.title = "iniciar sesion Bv"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    usuario_prueba= "player124"
    contrasena_prueba= "1020"

    username = ft.TextField(label="username", width=280)
    correo = ft.TextField(label="correo electronico", width=280)
    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=280
    )

    mensaje = ft.Text("")

    def pagina_principal():
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido al sistema", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Usuario: {username.value}")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def iniciar_sesion(e):

        if username.value == usuario_demo and contraseña.value == password_demo:
            pagina_principal()

        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    sesion = ft.Container(
        width=350,
        padding=30,
        border_radius=10,
        bgcolor="white",
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Text("Inicio de sesion", size=24, weight=ft.FontWeight.BOLD),
                username,
                correo,
                contraseña,

                ft.ElevatedButton(
                    "iniciar sesion",
                    width=280,
                    on_click=iniciar_sesion
                ),

                mensaje
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)
