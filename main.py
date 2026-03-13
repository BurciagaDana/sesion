import flet as ft

def main(page: ft.Page):
    page.title = "iniciar sesion Bv"
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
                ft.Text("Inicio de sesion ", size=24,  weight=ft.FontWeight.BOLD),
                
                ft.TextField(
                    label="username",
                    prefix_icon=ft.Icons.SENTIMENT_SATISFIED,
                    width=280,

            
                ),


                ft.TextField(
                    label="correo electronico",
                    prefix_icon=ft.Icons.FACE,   
                    width=280,

            
                ),

                ft.TextField(
                    label="Contraseña",
                    prefix_icon= ft.Icons.COOKIE,
        
                    password=True,
                    can_reveal_password=True,
                    width=280
                ),
                

                ft.Button(
                    content="iniciar sesion",
                    width=280,
                    bgcolor="#F171C7",
                    
                ),
                
                ft.Button(
                    content="registrarme",
                    width=280,
                    bgcolor="#0BF81E",
                    
                ),
                
                
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)
