import tkinter as tk
import x_func

class ShowCliente:
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

        self.ciLabel = tk.Label(self.mainMenu, text='Cedula', bg='white', font=('Helvetica', 16))
        self.ciLabel.grid(column=0, row=0, padx=10, pady=5)

        self.nomLabel = tk.Label(self.mainMenu, text='Nombre', bg='white', font=('Helvetica', 16))
        self.nomLabel.grid(column=1, row=0, padx=10, pady=5)

        self.apeLabel = tk.Label(self.mainMenu, text='Apellido', bg='white', font=('Helvetica', 16))
        self.apeLabel.grid(column=2, row=0, padx=10, pady=5)

        self.telLabel = tk.Label(self.mainMenu, text='Telefono', bg='white', font=('Helvetica', 16))
        self.telLabel.grid(column=3, row=0, padx=10, pady=5)

        self.showCli()

        self.mainWindow.mainloop()

    def showCli(self):
        cli = x_func.showCli() #Invocacion del CRUD para mostrar
        variables = [] #Creacion de una lista de variables para poder mostrar, NO TOCAAAAAAAAAR
        r = 1 #Variable de control
        for i in range(len(cli)): #Bucle para poder mostrar todos los proveedores independientemente de la cantidad
            col = 0
            for j in cli[i]:
                variables.append(col)
                variables[col] = tk.Label(self.mainMenu, text=j, bg='white', font=('Helvetica', 16))
                variables[col].grid(column=col, row=r, padx=10, pady=5)
                col += 1
            r += 1

    def reload(self):
        self.mainWindow.destroy()
        win = ShowCliente()
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
        from x_addinsumo import AddInsumo
        self.mainWindow.destroy()
        win = AddInsumo()
        win

    def showInsButton(self):
        from x_showinsumo import ShowInsumo
        self.mainWindow.destroy()
        win = ShowInsumo()
        win

    def addCliButton(self):
        from x_addcliente import AddCliente
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        from x_addcliente import AddCliente
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        from x_updateinsumo import UpdateInsumo
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        from x_showreceta import ShowReceta
        self.mainWindow.destroy()
        win = ShowReceta()
        win