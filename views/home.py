import tkinter as tk
from views.base import BaseView

#Clase para la ventana de inicio
class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        self.title1 = tk.Label(self, text='Bienvenido a', font=('Helvetica', 24, 'bold', 'italic'))
        self.title1.grid(row=0, column=1, sticky='w')
        self.title2 = tk.Label(self, text='Mon Amour', font=('Helvetica', 24, 'bold', 'italic'))
        self.title2.grid(row=1, column=1, sticky='w')