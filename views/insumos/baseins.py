import tkinter as tk
from views.base import BaseView

#Clase base para los insumos
class BaseInsView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Botones de navegacion entre las views de insumos
        self.showBtn = tk.Button(self, text='Mostrar', font=('Helvetica', 14), command=lambda: controller.show_view('ShowInsView'))
        self.showBtn.grid(row=0, column=0, sticky='w', padx=5)
        self.addBtn = tk.Button(self, text='Agregar', font=('Helvetica', 14))
        self.addBtn.grid(row=1, column=0, sticky='w', padx=5)