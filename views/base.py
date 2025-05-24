import tkinter as tk

class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(1, weight=1)

        self.homeBtn = tk.Button(self, text='Inicio', font=('Helvetica', 16), command=lambda: controller.show_view('HomeView'))
        self.homeBtn.grid(row=0, column=0, pady=5)
        self.provBtn = tk.Button(self, text='Prov', font=('Helvetica', 16), command=lambda: controller.show_view('ShowProvView'))
        self.provBtn.grid(row=1, column=0, pady=5)