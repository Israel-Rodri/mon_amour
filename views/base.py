import tkinter as tk

class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Crear barra de menú
        menubar = tk.Menu(self)
        self.winfo_toplevel().config(menu=menubar)

        # Menú principal
        menubar.add_command(label="Inicio", command=lambda: controller.show_view('HomeView'))
        menubar.add_command(label="Prov", command=lambda: controller.show_view('ShowProvView'))
        menubar.add_command(label="Ins", command=lambda: controller.show_view('ShowInsView'))

        # Elimina los botones laterales