import flet as ft
from controllers.ins_controller import InsController

#Creacion de la clase principal 
class InsView:
    #Inicializador, recibe como parametros datos que deben permanecer sin cambios aunque se refresque la vista
    def __init__(self, page, refresh_callback, selected_row_index=None, selected_row_data=None):
        self.page = page
        self.ins_model = InsController() #Instanciacion de la clase del controlador
        self.refresh_callback = refresh_callback #callback que permitre comunicacion entre main y esta vista
        self.selected_row_index = selected_row_index #Indice de la fila seleccionada en la tabla
        self.selected_row_data = selected_row_data #Datos de la fila seleccionada en la tabla
        self.unidades = ['Gr', 'Ml', 'Unidad', 'Kg', 'Lt', 'Mg']

    #Funcion que crea los elementos graficos iniciales, todo lo que se deberia ver al abrir la seccion TIENE que ir aqui
    def build(self):
        ins = self.ins_model.show_ins() #Funcion que retorna los datos almacenados de los insumos
        if isinstance(ins, str): #Confirmacion, en caso de que la funcion no retorne una lista (como deberia) devuelve una lista en blanco
            rows = []
            empty_message = ft.Text(ins)
        else:
            #Funcion para detectar la fila seleccionada
            def on_row_selected(e, ins, idx): 
                self.selected_row_data = ins
                self.refresh_callback(idx, ins) #Actualiza la vista para mostrar que fila esta seleccionada
                print(f'Fila seleccionada: {ins}') #Debug para ver la info seleccionada
                self.page.update()
            rows = [
                ft.DataRow(
                    cells=[
                        #Creacion dinamica de contenido para la tabla de insumos
                        ft.DataCell(ft.Text(str(ins[0]))),
                        ft.DataCell(ft.Text(str(ins[1]))),
                        ft.DataCell(ft.Text(str(ins[2]))),
                        ft.DataCell(ft.Text(str(ins[3]))),
                        ft.DataCell(ft.Text(str(ins[4]))),
                        ft.DataCell(ft.Text(str(ins[5]))),
                    ],
                    on_select_changed=lambda e, ins=ins, idx=idx: on_row_selected(e, ins, idx),
                    selected=(self.selected_row_index == idx)
                ) for idx, ins in enumerate(ins)
            ]
            empty_message = None

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.DataTable(
                                #Tabla dinamica de insumos
                                columns=[
                                    ft.DataColumn(label=ft.Text('Id')),
                                    ft.DataColumn(label=ft.Text('Nombre')),
                                    ft.DataColumn(label=ft.Text('Descripcion')),
                                    ft.DataColumn(label=ft.Text('Unidad de Medida')),
                                    ft.DataColumn(label=ft.Text('Cantidad')),
                                    ft.DataColumn(label=ft.Text('Precio Unitario'))
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
                                on_click=self.add_ins
                            ),
                            ft.ElevatedButton(
                                text='Editar',
                                width=120,
                                height=50,
                                bgcolor="#6D001A",
                                color="#FFFFFF",
                                on_click=self.edit_ins,
                            ),
                            ft.ElevatedButton(
                                text='Eliminar',
                                width=120,
                                height=50,
                                bgcolor="#6D001A",
                                color="#FFFFFF",
                                on_click=self.del_ins,
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

    #Funcion principal para crear insumo
    def add_ins(self, e):
        #Campos de texto para introducir datos
        nombre = ft.TextField(label='Nombre', max_length=30)
        descripcion = ft.TextField(label='Descripcion', max_length=100)
        unidad = ft.Dropdown(
            label='Unidad de Medida',
            options=[
                ft.dropdown.Option(u) for u in self.unidades
            ],
            width=300
        )
        cantidad = ft.TextField(label='Cantidad', max_length=10)
        precio = ft.TextField(label='Precio Unitario', max_length=15)

        #Ejecucion de las confirmaciones correspondientes
        nombre.on_change = lambda e: self.filter_input_inverse(nombre, '0123456789,.-;:_{+[¨*~]}')
        descripcion.on_change = lambda e: self.filter_input_inverse(descripcion, ',.-;:_{+[¨*~]}')
        cantidad.on_change = lambda e: self.filter_input(cantidad, '0123456789.')
        precio.on_change = lambda e: self.filter_input(precio, '0123456789.')

        #Funcion para mostrar un mensaje de exito o error, dependiendo del caso
        def show_add_result(success):
            if success == True:
                message = "Insumo agregado exitosamente ✅"
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

        #Funcion para confirmar y ejecutar la creacion de insumos
        def add_ins_method(ev):
            if nombre.value == '' or descripcion.value == '' or unidad.value == '' or cantidad.value == '' or precio.value == '':
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
                result = self.ins_model.add_ins(nombre.value.capitalize(), descripcion.value, unidad.value, float(cantidad.value), float(precio.value))
                dialog.open = False
                self.page.update()
                show_add_result(result)
                self.refresh_callback()

        #Creacion de la ventana para agregar insumos
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text('Agregar Insumo'),
            content=ft.Column([nombre, descripcion, unidad, cantidad, precio], tight=True),
            actions=[
                ft.TextButton('Cancelar', on_click=lambda e: (
                    setattr(dialog, 'open', False),
                    self.page.update()
                )),
                ft.ElevatedButton('Guardar', on_click=add_ins_method)
            ],
            actions_alignment='end'
        )
        dialog.open = True
        self.page.overlay.append(dialog)
        self.page.update()

    #Funcion principal para eliminar insumos
    def del_ins(self, e):
        if not self.selected_row_data:
            #Mensaje que se muestra en caso de que se presione el boton sin haber seleccionado una fila
            warning_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Advertencia"),
                content=ft.Text("Debe seleccionar un insumo antes de eliminar."),
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
            content=ft.Text("¿Desea eliminar el insumo seleccionado?"),
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

    #Funcion para eliminar insumos
    def confirm_delete(self, dialog):
        dialog.open = False
        self.page.update()

        result = self.ins_model.del_ins(self.selected_row_data)

        # Mostrar resultado
        if result == True:
            message = "Insumo eliminado exitosamente ✅"
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

    def edit_ins(self, e):
        if not self.selected_row_data:
            #Mensaje que se muestra en caso de que se presione el boton sin haber seleccionado una fila
            warning_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Advertencia"),
                content=ft.Text("Debe seleccionar un insumo antes de editar."),
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
        unidad_actual = self.selected_row_data[3].capitalize()
        id = ft.TextField(label='Id', value=self.selected_row_data[0], read_only=True)
        nombre = ft.TextField(label='Nombre', max_length=30, value=self.selected_row_data[1])
        descripcion = ft.TextField(label='Descripcion', max_length=100, value=self.selected_row_data[2])
        unidad = ft.Dropdown(
                    label='Unidad de Medida',
                    options=[
                        ft.dropdown.Option(u) for u in self.unidades
                    ],
                    value=unidad_actual,  # ← Esto preselecciona la unidad actual
                    width=300
                )
        cantidad = ft.TextField(label='Cantidad', max_length=10, value=self.selected_row_data[4])
        precio = ft.TextField(label='Precio Unitario', max_length=15, value=self.selected_row_data[5])

        #Ejecucion de las confirmaciones correspondientes
        nombre.on_change = lambda e: self.filter_input_inverse(nombre, '0123456789,.-;:_{+[¨*~]}')
        descripcion.on_change = lambda e: self.filter_input_inverse(descripcion, ',.-;:_{+[¨*~]}')
        cantidad.on_change = lambda e: self.filter_input(cantidad, '0123456789.')
        precio.on_change = lambda e: self.filter_input(precio, '0123456789.')

        #Funcion para mostrar un mensaje de exito o error, dependiendo del caso
        def show_edit_result(success):
            if success == True:
                message = "Insumo editado exitosamente ✅"
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

        #Funcion para confirmar y ejecutar la edicion de insumos
        def edit_ins_method(ev):
            if nombre.value == '' or descripcion.value == '' or unidad.value == '' or cantidad.value == '' or precio.value == '':
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
                result = self.ins_model.edit_ins(int(id.value), nombre.value.capitalize(), descripcion.value, unidad.value, float(cantidad.value), float(precio.value))
                dialog.open = False
                self.page.update()
                show_edit_result(result)
                self.refresh_callback()

        #Creacion de la ventana para editar insumos
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text('Editar Insumo'),
            content=ft.Column([id, nombre, descripcion, unidad, cantidad, precio], tight=True),
            actions=[
                ft.TextButton('Cancelar', on_click=lambda e: (
                    setattr(dialog, 'open', False),
                    self.page.update()
                )),
                ft.ElevatedButton('Guardar', on_click=edit_ins_method)
            ],
            actions_alignment='end'
        )
        dialog.open=True
        self.page.overlay.append(dialog)
        self.page.update()