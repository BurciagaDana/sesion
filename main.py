import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    sesion = ft.Container(
        width=350,
        padding=30,
        border_radius=10,
        bgcolor="white",
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Text("Iniciar sesión", size=24, weight="bold"),

                ft.TextField(
                    label="Correo electrónico",
                    prefix_icon=ft.Icons.FACE,   
                    width=280,

            
                ),

                ft.TextField(
                    label="Introduzca su contraseña",
                    password=True,
                    can_reveal_password=True,
                    width=280
                ),

                ft.Button(
                    content="Iniciar sesion",
                    width=280,
                    bgcolor="#08F31C",
                    
                ),
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)

