import tkinter as tk

class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sideMenu = tk.Frame(self, width=100, bg='#424242')
        self.sideMenu.grid(row=0, column=0, sticky='ns')

        self.homeBtn = tk.Button(self.sideMenu, text='Inicio', command=lambda: controller.show_view('HomeView'))
        self.homeBtn.grid(column=0, row=0, pady=5)

        self.showProvBtn = tk.Button(self.sideMenu, text='Mostrar Prov', command=lambda: controller.show_view('ShowProvView'))
        self.showProvBtn.grid(column=0, row=1, pady=5)