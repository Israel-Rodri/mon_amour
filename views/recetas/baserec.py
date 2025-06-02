import tkinter as tk
from views.base import BaseView

#Clase base para los proveedores
class BaseRecView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Botones de navegacion entre las views de proveedores
        self.showBtn = tk.Button(self, text='Mostrar', font=('Helvetica', 14), bg='#7e00a8', fg='white', command=lambda: controller.show_view('ShowRecView'))
        self.showBtn.place(x=10, y=260)
        self.addBtn = tk.Button(self, text='Agregar', font=('Helvetica', 14), bg='#7e00a8', fg='white', command=lambda: controller.show_view('AddRecView'))
        self.addBtn.place(x=10, y=310)
        self.updBtn = tk.Button(self, text='Actualizar', font=('Helvetica', 14), bg='#7e00a8', fg='white', command=lambda: controller.show_view('UpdRecView'))
        self.updBtn.place(x=10, y=360)