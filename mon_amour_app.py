import tkinter as tk
from models.provmodels import Model
from views.provviews import View
from controllers.provcontroller import Controller

mainWindow = tk.Tk()
mainWindow.resizable(width=False, height=False)
modelo = Model()
vista = View(mainWindow)
controlador = Controller(modelo)
vista.set_controller(controlador)

if __name__ == '__main__':
    app = vista
    app.mainloop()