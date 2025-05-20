import tkinter as tk
from tkinter import messagebox
from models.provmodels import Model
from views.prov.addview import AddView
from controllers.provcontroller import Controller

mainWindow = tk.Tk()
mainWindow.resizable(width=False, height=False)
modelo = Model()
vista = AddView(mainWindow)
controlador = Controller(modelo)
vista.set_controller(controlador)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning('Arreglar', 'Eliminar messagebox del main\nVer como hacer el cambio de pestañas')
    app = vista
    app.mainloop()