import tkinter as tk
from tkinter import messagebox
from x_gui import AddInsumo, ShowInsumo, AddCliente, ShowCliente, AddReceta, UpdateInsumo, ShowReceta

class Home:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title('Mon Amour')
        self.mainWindow.geometry('1200x750')
        self.mainWindow.resizable(False, False)
        
        #Creacion del menu lateral
        self.sideMenu = tk.Frame(self.mainWindow, width=100, bg='lightgrey')
        self.sideMenu.pack(side='left', fill='y')

        self.sideAddProvButton = tk.Button(self.sideMenu, text='Agregar Proveedor', bg='white', font=('Helvetica', 10), command=self.addProvButton)
        self.sideAddProvButton.grid(column=0, row=0, pady=10, padx=5)

        self.sideShowProvButton = tk.Button(self.sideMenu, text='Mostrar Proveedores', bg='white', font=('Helvetica', 10), command=self.showProvButton)
        self.sideShowProvButton.grid(column=0, row=1, pady=10, padx=5)

        self.sideAddInsButton = tk.Button(self.sideMenu, text='Agregar Insumo', bg='white', font=('Helvetica', 10), command=self.addInsButton)
        self.sideAddInsButton.grid(column=0, row=2, pady=10, padx=5)

        self.sideShowInsButton = tk.Button(self.sideMenu, text='Mostrar Insumos', bg='white', font=('Helvetica', 10), command=self.showInsButton)
        self.sideShowInsButton.grid(column=0, row=3, pady=10, padx=5)

        self.sideAddCliButton = tk.Button(self.sideMenu, text='Agregar Clientes', bg='white', font=('Helvetica', 10), command=self.addCliButton)
        self.sideAddCliButton.grid(column=0, row=4, pady=10, padx=5)

        self.sideShowCliButton = tk.Button(self.sideMenu, text='Mostrar Clientes', bg='white', font=('Helvetica', 10), command=self.showCliButton)
        self.sideShowCliButton.grid(column=0, row=5, pady=10, padx=5)

        self.sideShowCliButton = tk.Button(self.sideMenu, text='Mostrar Clientes', bg='white', font=('Helvetica', 10), command=self.showCliButton)
        self.sideShowCliButton.grid(column=0, row=5, pady=10, padx=5)

        self.sideAddRecButton = tk.Button(self.sideMenu, text='Agregar Receta', bg='white', font=('Helvetica', 10), command=self.addRecButton)
        self.sideAddRecButton.grid(column=0, row=6, pady=10, padx=5)

        self.sideUpdateInsButton = tk.Button(self.sideMenu, text='Actualizar Insumo', bg='white', font=('Helvetica', 10), command=self.updateInsButton)
        self.sideUpdateInsButton.grid(column=0, row=7, pady=10, padx=5)

        self.sideShowRecButton = tk.Button(self.sideMenu, text='Mostrar Recetas', bg='white', font=('Helvetica', 10), command=self.showRecButton)
        self.sideShowRecButton.grid(column=0, row=8, pady=10, padx=5)

        self.sideReloadButton = tk.Button(self.sideMenu, text='Recargar', bg='white', font=('Helvetica', 10), command=self.reload)
        self.sideReloadButton.grid(column=0, row=9, pady=10, padx=5)

        #Creacion del menu principal
        self.mainMenu = tk.Frame(self.mainWindow, bg='white')
        self.mainMenu.pack(fill='both', side='right', expand=True)

        self.titleMenu = tk.Frame(self.mainMenu, bg='white')
        self.titleMenu.pack(expand=True)

        self.title1 = tk.Label(self.titleMenu, text='Bienvenido(a)', bg='white', font=('Helvetica', 30))
        self.title1.pack()

        self.title2 = tk.Label(self.titleMenu, text='A la aplicación de gestión de insumos', bg='white', font=('Helvetica', 25))
        self.title2.pack()

        self.title3 = tk.Label(self.titleMenu, text='De la pastelería Mon Amour', bg='white', font=('Helvetica', 30))
        self.title3.pack()

        self.mainWindow.mainloop()

    def reload(self):
        self.mainWindow.destroy()
        win = Home()
        win

    def addProvButton(self):
        from x_addProv import AddProveedor
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
        from x_showprov import ShowProveedor
        self.mainWindow.destroy()
        win = ShowProveedor()
        win

    def addInsButton(self):
        self.mainWindow.destroy()
        win = AddInsumo()
        win

    def showInsButton(self):
        self.mainWindow.destroy()
        win = ShowInsumo()
        win

    def addCliButton(self):
        self.mainWindow.destroy()
        win = AddCliente
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddReceta()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

def errorMessage(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Ocurrio un error', message)

win = Home()
win