import tkinter as tk
from views.prov.baseprov import BaseProvView

class ShowProvView(BaseProvView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        self.title = tk.Label(self, text='Mostrar Proveedores', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        prov = controller.showProv()

        headers = ['Rif', 'Nombre', 'Teléfono', 'Email']
        for col, header in enumerate(headers):
            tk.Label(self, text=header, font=('Helvetica', 14, 'bold')).grid(row=1, column=col+1, padx=5, sticky='w')

        for row, tupla in enumerate(prov, start=2):
            for col, dato in enumerate(tupla):
                tk.Label(self, text=dato, font=('Helvetica', 12)).grid(row=row, column=col+1, padx=5, sticky='w')