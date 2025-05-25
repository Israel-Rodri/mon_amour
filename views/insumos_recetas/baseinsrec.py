import tkinter as tk
from views.base import BaseView

#Clase base para los proveedores
class BaseInsRecView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Botones de navegacion entre las views de proveedores
        self.showBtn = tk.Button(self, text='Mostrar', font=('Helvetica', 14), command=lambda: controller.show_view('ShowInsRecView'))
        self.showBtn.grid(row=0, column=0, sticky='w', padx=5)