import tkinter as tk
from views.base import BaseView

#Clase base para los proveedores
class BaseRecView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Botones de navegacion entre las views de proveedores
        self.showBtn = tk.Button(self, text='Mostrar', font=('Helvetica', 14), command=lambda: controller.show_view('ShowRecView'))
        self.showBtn.grid(row=0, column=0, sticky='w', padx=5)
        self.addBtn = tk.Button(self, text='Agregar', font=('Helvetica', 14), command=lambda: controller.show_view('AddRecView'))
        self.addBtn.grid(row=1, column=0, sticky='w', padx=5)
        self.updBtn = tk.Button(self, text='Actualizar', font=('Helvetica', 14), command=lambda: controller.show_view('UpdRecView'))
        self.updBtn.grid(row=2, column=0, sticky='w', padx=5)