import tkinter as tk
from views.base import BaseView

class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        self.x = tk.Label(self, text='Prieba', font=('Helvetica', 24), fg='red')
        self.x.grid(row=1, column=1, sticky='w')