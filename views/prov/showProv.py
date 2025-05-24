import tkinter as tk
from views.base import BaseView

class ShowProvView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        self.title = tk.Label(self, text='Mostrar Proveedores', font=('Helvetica', 18))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        prov = controller.show()

        self.provList = tk.Label(self, text=prov, font=('Helvetica', 14))
        self.provList.grid(column=1, row=1, pady=5, sticky='w')