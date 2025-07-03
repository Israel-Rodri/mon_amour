import flet as ft
from controllers.prov_controller import ProvController

class ProvView:
    def __init__(self, page):
        self.page = page
        self.prov_model = ProvController()

    def build(self):
        provs = self.prov_model.show_prov()
        if isinstance(provs, str):
            rows = []
            empty_message = ft.Text(provs)
        else:
            rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(prov[0]))),
                        ft.DataCell(ft.Text(str(prov[1]))),
                        ft.DataCell(ft.Text(str(prov[2]))),
                        ft.DataCell(ft.Text(str(prov[3])))
                    ]
                ) for prov in provs
            ]
            empty_message = None

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(label=ft.Text('Rif')),
                                    ft.DataColumn(label=ft.Text('Nombre')),
                                    ft.DataColumn(label=ft.Text('Telefono')),
                                    ft.DataColumn(label=ft.Text('Email'))
                                ],
                                rows=rows,
                            )
                        ]
                    ),
                    empty_message if empty_message else ft.Container(),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text='Agregar',
                                width=120,
                                height=50,
                                bgcolor="#6D001A",
                                color="#FFFFFF",
                                on_click=self.add_prov
                            ),
                            ft.ElevatedButton(
                                text='Editar',
                                width=120,
                                height=50,
                                bgcolor="#6D001A",
                                color="#FFFFFF",
                            ),
                            ft.ElevatedButton(
                                text='Eliminar',
                                width=120,
                                height=50,
                                bgcolor="#6D001A",
                                color="#FFFFFF",
                            )
                        ],
                        alignment='center'
                    ),
                ]
            ),
        )

    def add_prov(self, e):
        rif = ft.TextField(label='Rif')
        nom = ft.TextField(label='Nombre')
        tel = ft.TextField(label='Telefono')
        email = ft.TextField(label='Email')

        def show_result(success: bool):
            if success:
                message = "Proveedor agregado exitosamente ✅"
                bgcolor = "#4CAF50"  # verde éxito
            else:
                message = "Error al agregar proveedor ❌"
                bgcolor = "#F44336"  # rojo error

            result_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Resultado"),
                content=ft.Text(message),
                bgcolor=bgcolor,
                actions=[
                    ft.TextButton("Cerrar", on_click=lambda e: (
                        setattr(result_dialog, "open", False),
                        self.page.update()
                    ))
                ],
                actions_alignment="end"
            )
            result_dialog.open = True
            self.page.overlay.append(result_dialog)
            self.page.update()

        def add_prov_method(ev):
            if rif.value == '' or nom.value == '' or tel.value == '' or email.value == '':
                empty_dialog = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Error"),
                    content=ft.Text("Debe rellenar todos los campos"),
                    actions=[
                        ft.TextButton('Cerrar', on_click=lambda e: (
                            setattr(empty_dialog, "open", False),
                            self.page.update()
                        ))
                    ],
                    actions_alignment="end"
                )
                empty_dialog.open = True
                self.page.overlay.append(empty_dialog)
                self.page.update()
            else:
                result = self.prov_model.add_prov(rif.value, nom.value, tel.value, email.value)
                dialog.open = False
                self.page.update()
                show_result(result)

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text('Agregar Proveedor'),
            content=ft.Column([rif, nom, tel, email], tight=True),
            actions=[
                ft.TextButton('Cancelar', on_click=lambda e: (
                    setattr(dialog, 'open', False),
                    self.page.update()
                )),
                ft.ElevatedButton('Guardar', on_click=add_prov_method)
            ],
            actions_alignment='end'
        )
        dialog.open = True
        self.page.overlay.append(dialog)
        self.page.update()