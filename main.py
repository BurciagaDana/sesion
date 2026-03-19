
import flet as ft

def main(page: ft.Page):
    page.title = "iniciar sesion Bv"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    usuario_prueba= "player124"
    contraseña_prueba= "1020"
    correo_prueba= "player124@gmail.com"

    username = ft.TextField(
       label="username", 
       width=280,
       prefix_icon=ft.Icons.FACE
       )
    correo = ft.TextField(
    label="correo electronico", 
    width=280,
    prefix_icon=ft.Icons.ALTERNATE_EMAIL
    )
    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        prefix_icon=ft.Icons.PASSWORD
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
     if (
        username.value == usuario_prueba and
        contraseña.value == contraseña_prueba and
        correo.value == correo_prueba
    ):
        pagina_principal()
     else:
        mensaje.value = "Usuario, correo o contraseña incorrectos"
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
                    on_click=iniciar_sesion,
                  style=ft.ButtonStyle(
    bgcolor={
        ft.ControlState.DEFAULT: "#4C7AAF",
        ft.ControlState.HOVERED: "#3a4498"
    },
    color="white"
)
                ),

                mensaje
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)
