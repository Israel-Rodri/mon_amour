import tkinter as tk
from views.base import BaseView

#Clase para la ventana de inicio
class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        self.title1 = tk.Label(self, text='Bienvenido a', font=('Helvetica', 24, 'bold', 'italic'))
        self.title1.place(x=300, y=200)
        self.title2 = tk.Label(self, text='Mon Amour', font=('Helvetica', 24, 'bold', 'italic'))
        self.title2.place(x=300, y=260)