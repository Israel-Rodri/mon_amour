import flet as ft

def otherView():
    other = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text('Produccion', size=50),
                ft.Row(
                    controls=[
                        ft.Image(src='images/mon_amour_logo.jpeg')
                    ]
                ),
            ],
        ),
    )
    return other