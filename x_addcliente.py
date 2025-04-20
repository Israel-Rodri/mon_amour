import tkinter as tk
import x_func

class AddCliente:
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

        self.ciCliLabel = tk.Label(self.mainMenu, text='Cedula del cliente:', bg='white', font=('Helvetica', 18))
        self.ciCliLabel.grid(column=0, row=0, pady=5)
        self.ciCliEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.ciCliEntry.grid(column=1, row=0, pady=5)

        self.nomCliLabel = tk.Label(self.mainMenu, text='Nombre del cliente:', bg='white', font=('Helvetica', 18))
        self.nomCliLabel.grid(column=0, row=1, pady=5)
        self.nomCliEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.nomCliEntry.grid(column=1, row=1, pady=5)

        self.apeCliLabel = tk.Label(self.mainMenu, text='Apellido del cliente:', bg='white', font=('Helvetica', 18))
        self.apeCliLabel.grid(column=0, row=2, pady=5)
        self.apeCliEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.apeCliEntry.grid(column=1, row=2, pady=5)

        self.telCliLabel = tk.Label(self.mainMenu, text='Telefono del cliente:', bg='white', font=('Helvetica', 18))
        self.telCliLabel.grid(column=0, row=3, pady=5)
        self.telCliEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.telCliEntry.grid(column=1, row=3, pady=5)

        self.addCliButton = tk.Button(self.mainMenu, text='Agregar Cliente', bg='lightgrey', font=('Helvetica', 14), command=self.addCli)
        self.addCliButton.grid(column=0, row=4, pady=5)

        self.mainWindow.mainloop()

    def addCli(self):
        from x_home import errorMessage
        ci = self.ciCliEntry.get()
        if ci == '':
            errorMessage('Cedula de cliente no puede estar vacio')
            self.reload()
        ciNum = int(ci)
        nom = self.nomCliEntry.get()
        if nom == '':
            errorMessage('Nombre de cliente no puede estar vacio')
            self.reload()
        ape = self.apeCliEntry.get()
        if ape == '':
            errorMessage('Apellido cliente no puede estar vacio')
            self.reload()
        tel = self.telCliEntry.get()
        if tel == '':
            errorMessage('Telefono cliente no puede estar vacio')
            self.reload()
        x_func.addCli(ciNum, nom.capitalize(), ape.capitalize(), tel)
        self.ciCliEntry.delete(0, tk.END)
        self.nomCliEntry.delete(0, tk.END)
        self.apeCliEntry.delete(0, tk.END)
        self.telCliEntry.delete(0, tk.END)

    def reload(self):
        self.mainWindow.destroy()
        win = AddCliente()
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
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def showCliButton(self):
        from x_showcliente import ShowCliente
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        from x_addreceta import AddReceta
        self.mainWindow.destroy()
        win = AddReceta()
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