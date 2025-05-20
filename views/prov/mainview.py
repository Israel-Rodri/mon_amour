import tkinter as tk
from tkinter import messagebox

class View(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry('800x600')

        self.provMenu = tk.Menu(self.root)

        self.provMenuOptions = tk.Menu(self.provMenu, tearoff=0)
        self.provMenuOptions.add_command(label='Mostrar')
        self.provMenuOptions.add_command(label='Agregar')
        self.provMenuOptions.add_command(label='Actualizar')
        self.provMenuOptions.add_command(label='Eliminar')

        self.provMenu.add_cascade(label='Proveedores', menu=self.provMenuOptions)

        self.root.config(menu=self.provMenu)

    def set_controller(self, controller):
        self.controller = controller