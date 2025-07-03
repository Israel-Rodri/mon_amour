import tkinter as tk
from views.insumos.baseins import BaseInsView

#Clase para mostrar los insumos
class ShowInsView(BaseInsView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Titulo de la seccion
        self.title = tk.Label(self, text='Mostrar Insumos', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        headers = ['Nombre', 'Descripcion', 'Medida', 'Cantidad', 'Precio']
        for col, header in enumerate(headers):
            tk.Label(self, text=header, font=('Helvetica', 14, 'bold')).grid(row=1, column=col+1, padx=5, sticky='w')

#Lista de los datos a mostrar, util para la autoactualizacion
        self.dataLabels = []

    #Funcion para destruir datos para autoactualizar
    def onShow(self):
        # Elimina los labels de datos anteriores
        for label in self.dataLabels:
            label.destroy()
        self.dataLabels.clear()

        #Llamado a la funcion para obtener los datos de la BD
        ins = self.controller.showIns()

        #Bucle para agregar todos los datos obtenidos en pantalla
        for row, tupla in enumerate(ins, start=2):
            for col, dato in enumerate(tupla):
                if col != 0 and col < 5:
                    label = tk.Label(self, text=dato, font=('Helvetica', 12))
                    label.grid(row=row, column=col, padx=5, sticky='w')
                    self.dataLabels.append(label)
                elif col != 5 and col > 5:
                    label = tk.Label(self, text=dato, font=('Helvetica', 12))
                    label.grid(row=row, column=col-1, padx=5, sticky='w')
                    self.dataLabels.append(label)
                else:
                    pass