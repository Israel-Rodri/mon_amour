import tkinter as tk
from views.insumos.baseins import BaseInsView

class ShowInsView(BaseInsView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        self.title = tk.Label(self, text='Mostrar Insumos', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        ins = controller.showIns()

        headers = ['Nombre', 'Descripcion', 'Medida', 'Cantidad', 'Precio']
        for col, header in enumerate(headers):
            tk.Label(self, text=header, font=('Helvetica', 14, 'bold')).grid(row=1, column=col+1, padx=5, sticky='w')

        for row, tupla in enumerate(ins, start=2):
            for col, dato in enumerate(tupla):
                if col != 0 and col != 5:
                    tk.Label(self, text=dato, font=('Helvetica', 12)).grid(row=row, column=col, padx=5, sticky='w')
                else:
                    pass