import tkinter as tk

#Clase base para todas las views
class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #Creacion de barra de menu, el menu superior
        menubar = tk.Menu(self)
        self.winfo_toplevel().config(menu=menubar)

        #Botones del menu
        menubar.add_command(label="Inicio", command=lambda: controller.show_view('HomeView'))
        menubar.add_command(label="Prov", command=lambda: controller.show_view('ShowProvView'))
        menubar.add_command(label="Ins", command=lambda: controller.show_view('ShowInsView'))