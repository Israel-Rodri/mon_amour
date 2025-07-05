import flet as ft
from controllers.prov_controller import ProvController

#Creacion de la clase principal 
class ProvView:
    #Inicializador, recibe como parametros datos que deben permanecer sin cambios aunque se refresque la vista
    def __init__(self, page, refresh_callback, selected_row_index=None, selected_row_data=None):
        self.page = page
        self.prov_model = ProvController() #Instanciacion de la clase del controlador
        self.refresh_callback = refresh_callback #callback que permitre comunicacion entre main y esta vista
        self.selected_row_index = selected_row_index #Indice de la fila seleccionada en la tabla
        self.selected_row_data = selected_row_data #Datos de la fila seleccionada en la tabla

    #Funcion que crea los elementos graficos iniciales, todo lo que se deberia ver al abrir la seccion TIENE que ir aqui
    def build(self):
        provs = self.prov_model.show_prov() #Funcion que retorna los datos almacenados de los proveedores
        if isinstance(provs, str): #Confirmacion, en caso de que la funcion no retorne una lista (como deberia) devuelve una lista en blanco
            rows = []
            empty_message = ft.Text(provs)
        else:
            #Funcion para detectar la fila seleccionada
            def on_row_selected(e, prov, idx): 
                self.selected_row_data = prov
                self.refresh_callback(idx, prov) #Actualiza la vista para mostrar que fila esta seleccionada
                print(f'Fila seleccionada: {prov}') #Debug para ver la info seleccionada
                self.page.update()
            rows = [
                ft.DataRow(
                    cells=[
                        #Creacion dinamica de contenido para la tabla de proveedores
                        ft.DataCell(ft.Text(str(prov[0]))),
                        ft.DataCell(ft.Text(str(prov[1]))),
                        ft.DataCell(ft.Text(str(prov[2]))),
                        ft.DataCell(ft.Text(str(prov[3])))
                    ],
                    on_select_changed=lambda e, prov=prov, idx=idx: on_row_selected(e, prov, idx),
                    selected=(self.selected_row_index == idx)
                ) for idx, prov in enumerate(provs)
            ]
            empty_message = None

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.DataTable(
                                #Tabla dinamica de proveedores
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
                            #Botones de agregar, editar y eliminar
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
                                on_click=self.edit_prov,
                            ),
                            ft.ElevatedButton(
                                text='Eliminar',
                                width=120,
                                height=50,
                                bgcolor="#6D001A",
                                color="#FFFFFF",
                                on_click=self.del_prov,
                            )
                        ],
                        alignment='center'
                    ),
                ]
            ),
        )

    #Filtro para impedir escribir caracteres que NO sean los especificados
    def filter_input(self, textfield, allowed_chars):
        filtered = ''.join([c for c in textfield.value if c in allowed_chars])
        if textfield.value != filtered:
            textfield.value = filtered
            textfield.update()

    #Filtro para impedir escribir caracteres que SEAN los especificados
    def filter_input_inverse(self, textfield, excluded_chars):
        filtered = ''.join([c for c in textfield.value if c not in excluded_chars])
        if textfield.value != filtered:
            textfield.value = filtered
            textfield.update()

    #Funcion principal para crear proveedor
    def add_prov(self, e):
        #Campos de texto para introducir datos
        rif = ft.TextField(label='Rif', max_length=10)
        nom = ft.TextField(label='Nombre', max_length=30)
        tel = ft.TextField(label='Telefono', max_length=12)
        email = ft.TextField(label='Email', max_length=35)

        #Ejecucion de las confirmaciones correspondientes
        rif.on_change = lambda e: self.filter_input(rif, '01234567890-vVjJ')
        nom.on_change = lambda e: self.filter_input_inverse(nom, '01234567890,.-;:_{+´[¨*~]}')
        tel.on_change = lambda e: self.filter_input(tel, '1234567890-')
        email.on_change = lambda e: self.filter_input_inverse(email, 'áéíóúäëïöüÁÉÍÓÚÄËÏÖÜ*+{}[]?¿!¡')

        #Funcion para mostrar un mensaje de exito o error, dependiendo del caso
        def show_add_result(success):
            if success == True:
                message = "Proveedor agregado exitosamente ✅"
                bgcolor = "#4CAF50"  
            else:
                message = success
                bgcolor = "#F44336"  

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

        #Funcion para confirmar y ejecutar la creacion de proveedores
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
                show_add_result(result)
                self.refresh_callback()

        #Creacion de la ventana pata agregar proveedores
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

    #Funcion principal para eliminar proveedores
    def del_prov(self, e):
        if not self.selected_row_data:
            #Mensaje que se muestra en caso de que se presione el boton sin haber seleccionado una fila
            warning_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Advertencia"),
                content=ft.Text("Debe seleccionar un proveedor antes de eliminar."),
                actions=[
                    ft.TextButton("Cerrar", on_click=lambda e: (
                        setattr(warning_dialog, "open", False),
                        self.page.update()
                    ))
                ],
                actions_alignment="end"
            )
            warning_dialog.open = True
            self.page.overlay.append(warning_dialog)
            self.page.update()
            return

        #Ventana de confirmacion de eliminacion
        confirm_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmación"),
            content=ft.Text("¿Desea eliminar el proveedor seleccionado?"),
            actions=[
                ft.TextButton("No", on_click=lambda e: (
                    setattr(confirm_dialog, "open", False),
                    self.page.update()
                )),
                ft.ElevatedButton("Sí", bgcolor="#B71C1C", color="#FFFFFF", on_click=lambda e: self.confirm_delete(confirm_dialog))
            ],
            actions_alignment="end"
        )
        confirm_dialog.open = True
        self.page.overlay.append(confirm_dialog)
        self.page.update()

    #Funcion para eliminar proveedores
    def confirm_delete(self, dialog):
        dialog.open = False
        self.page.update()

        result = self.prov_model.del_prov(self.selected_row_data)

        # Mostrar resultado
        if result == True:
            message = "Proveedor eliminado exitosamente ✅"
            bgcolor = "#4CAF50"
        else:
            message = f"Error al eliminar: {result}"
            bgcolor = "#F44336"

        result_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Resultado"),
            content=ft.Text(message),
            bgcolor=bgcolor,
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: (
                    setattr(result_dialog, "open", False),
                    self.refresh_callback()  # Refresca la vista
                ))
            ],
            actions_alignment="end"
        )
        result_dialog.open = True
        self.page.overlay.append(result_dialog)
        self.page.update()

    def edit_prov(self, e):
        if not self.selected_row_data:
            #Mensaje que se muestra en caso de que se presione el boton sin haber seleccionado una fila
            warning_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Advertencia"),
                content=ft.Text("Debe seleccionar un proveedor antes de editar."),
                actions=[
                    ft.TextButton("Cerrar", on_click=lambda e: (
                        setattr(warning_dialog, "open", False),
                        self.page.update()
                    ))
                ],
                actions_alignment="end"
            )
            warning_dialog.open = True
            self.page.overlay.append(warning_dialog)
            self.page.update()
            return
        
        #Campos de texto para introducir datos
        rif = ft.TextField(label='Rif', max_length=10, value=self.selected_row_data[0], read_only=True)
        nom = ft.TextField(label='Nombre', max_length=30, value=self.selected_row_data[1])
        tel = ft.TextField(label='Telefono', max_length=12, value=self.selected_row_data[2])
        email = ft.TextField(label='Email', max_length=35, value=self.selected_row_data[3])

        #Ejecucion de las confirmaciones correspondientes
        rif.on_change = lambda e: self.filter_input(rif, '01234567890-vVjJ')
        nom.on_change = lambda e: self.filter_input_inverse(nom, '01234567890,.-;:_{+´[¨*~]}')
        tel.on_change = lambda e: self.filter_input(tel, '1234567890-')
        email.on_change = lambda e: self.filter_input_inverse(email, 'áéíóúäëïöüÁÉÍÓÚÄËÏÖÜ*+{}[]?¿!¡')

        #Funcion para mostrar un mensaje de exito o error, dependiendo del caso
        def show_edit_result(success):
            if success == True:
                message = "Proveedor agregado exitosamente ✅"
                bgcolor = "#4CAF50"  
            else:
                message = success
                bgcolor = "#F44336"  

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

        #Funcion para confirmar y ejecutar la creacion de proveedores
        def edit_prov_method(ev):
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
                result = self.prov_model.edit_prov(rif.value, nom.value, tel.value, email.value)
                dialog.open = False
                self.page.update()
                show_edit_result(result)
                self.refresh_callback()

        #Creacion de la ventana pata agregar proveedores
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text('Editar Proveedor'),
            content=ft.Column([rif, nom, tel, email], tight=True),
            actions=[
                ft.TextButton('Cancelar', on_click=lambda e: (
                    setattr(dialog, 'open', False),
                    self.page.update()
                )),
                ft.ElevatedButton('Guardar', on_click=edit_prov_method)
            ],
            actions_alignment='end'
        )
        dialog.open = True
        self.page.overlay.append(dialog)
        self.page.update()