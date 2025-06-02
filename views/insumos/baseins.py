import tkinter as tk
from views.base import BaseView

#Clase base para los insumos
class BaseInsView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Botones de navegacion entre las views de insumos
        self.showBtn = tk.Button(self, text='Mostrar', font=('Helvetica', 14), bg='#7e00a8', fg='white', command=lambda: controller.show_view('ShowInsView'))
        self.showBtn.place(x=10, y=260)
        self.addBtn = tk.Button(self, text='Agregar', font=('Helvetica', 14), bg='#7e00a8', fg='white', command=lambda: controller.show_view('AddInsView'))
        self.addBtn.place(x=10, y=310)
        self.updBtn = tk.Button(self, text='Actualizar', font=('Helvetica', 14), bg='#7e00a8', fg='white', command=lambda: controller.show_view('UpdInsView'))
        self.updBtn.place(x=10, y=360)