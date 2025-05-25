import tkinter as tk
from views.base import BaseView

class BaseProvView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        self.showBtn = tk.Button(self, text='Mostrar', font=('Helvetica', 14), command=lambda: controller.show_view('ShowProvView'))
        self.showBtn.grid(row=0, column=0, sticky='w', padx=5)
        self.addBtn = tk.Button(self, text='Agregar', font=('Helvetica', 14), command=lambda: controller.show_view('AddProvView'))
        self.addBtn.grid(row=1, column=0, sticky='w', padx=5)