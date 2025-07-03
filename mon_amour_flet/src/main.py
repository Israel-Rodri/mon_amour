import flet as ft
from views.prov_view import ProvView
from views.other_view import otherView

def main(page: ft.Page):
    page.title = 'Mon Amour - Gestión de Inventario'
    page.window_width = 1080
    page.window_height = 720
    page.theme_mode = ft.ThemeMode.LIGHT

    # Contenedor para la vista dinámica
    main_view = ft.Container(expand=True)

    # Funciones para cambiar la vista
    def show_inicio(e=None):
        main_view.content = ft.Text("Vista de Inicio", size=30)
        page.update()

    def show_proveedores(e=None):
        main_view.content = ProvView(page).build()
        page.update()

    def show_insumos(e=None):
        main_view.content = ft.Text("Vista de Insumos", size=30)
        page.update()

    def show_recetas(e=None):
        main_view.content = ft.Text("Vista de Recetas", size=30)
        page.update()

    def show_produccion(e=None):
        main_view.content = otherView()
        page.update()

    nav_items = [
        ("Inicio", show_inicio),
        ("Proveedores", show_proveedores),
        ("Insumos", show_insumos),
        ("Recetas", show_recetas),
        ("Produccion", show_produccion),
    ]

    nav_bar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value='Logo', size=20, weight='Bold', color='#FFFFFF'),
                *[
                    ft.ElevatedButton(
                        text=item[0],
                        on_click=item[1],
                        style=ft.ButtonStyle(
                            bgcolor="#6D001A",
                            color="#FFFFFF"
                        )
                    ) for item in nav_items
                ],
            ],
            spacing=10
        ),
        width=200,
        bgcolor='#6D001A',
        padding=10,
        border_radius=10
    )

    # Vista inicial
    show_inicio()

    page.add(
        ft.Row(
            controls=[nav_bar, main_view],
            expand=True
        )
    )

ft.app(main, assets_dir='assets')