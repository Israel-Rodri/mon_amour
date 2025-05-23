import tkinter as tk
from views.base import BaseView

class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        self.homeTitle1 = tk.Label(self, text='Bienvenido a la aplicación', font=('Helvetica', 24))
        self.homeTitle1.grid(row=1, column=1, pady=5)
        self.homeTitle2 = tk.Label(self, text='Mon Amour', font=('Helvetica', 24))
        self.homeTitle2.grid(row=2, column=1, pady=5)