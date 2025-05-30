import tkinter as tk
from views.login.baselogin import BaseLoginView

#Clase base para todas las views
class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.winfo_toplevel().config(menu=None)

        self.createMenu()

    def createMenu(self):
        self.winfo_toplevel().config(menu=None)
        if not isinstance(self, BaseLoginView) and BaseLoginView.login:
            #Creacion de barra de menu, el menu superior
            menubar = tk.Menu(self)
            self.winfo_toplevel().config(menu=menubar)

            #Botones del menu
            menubar.add_command(label="Inicio", command=lambda: self.controller.show_view('HomeView'))
            menubar.add_command(label="Proveedores", command=lambda: self.controller.show_view('ShowProvView'))
            menubar.add_command(label="Insumos", command=lambda: self.controller.show_view('ShowInsView'))
            menubar.add_command(label="Recetas", command=lambda: self.controller.show_view('ShowRecView'))
            menubar.add_command(label="Insumos Recetas", command=lambda: self.controller.show_view('ShowInsRecView'))

    def onShow(self):
        self.winfo_toplevel().config(menu=None)
        self.createMenu()