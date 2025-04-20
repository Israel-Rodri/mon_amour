import tkinter as tk
import x_func

class AddInsumo:
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

        self.nomInsLabel = tk.Label(self.mainMenu, text='Nombre del insumo:', bg='white', font=('Helvetica', 18))
        self.nomInsLabel.grid(column=0, row=0, pady=5)
        self.nomInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.nomInsEntry.grid(column=1, row=0, pady=5)

        self.descInsLabel = tk.Label(self.mainMenu, text='Breve descripcion del insumo:', bg='white', font=('Helvetica', 18))
        self.descInsLabel.grid(column=0, row=1, pady=5)
        self.descInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.descInsEntry.grid(column=1, row=1, pady=5)

        self.medInsLabel = tk.Label(self.mainMenu, text='Medida del insumo:', bg='white', font=('Helvetica', 18))
        self.medInsLabel.grid(column=0, row=2, pady=5)
        self.medInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.medInsEntry.grid(column=1, row=2, pady=5)

        self.canInsLabel = tk.Label(self.mainMenu, text='Cantidad actual del insumo:', bg='white', font=('Helvetica', 18))
        self.canInsLabel.grid(column=0, row=3, pady=5)
        self.canInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.canInsEntry.grid(column=1, row=3, pady=5)

        self.rifInsLabel = tk.Label(self.mainMenu, text='Rif del proveedor del insumo:', bg='white', font=('Helvetica', 18))
        self.rifInsLabel.grid(column=0, row=4, pady=5)
        self.rifInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.rifInsEntry.grid(column=1, row=4, pady=5)

        self.preInsLabel = tk.Label(self.mainMenu, text='Precio unitario del insumo:', bg='white', font=('Helvetica', 18))
        self.preInsLabel.grid(column=0, row=5, pady=5)
        self.preInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.preInsEntry.grid(column=1, row=5, pady=5)

        self.addInsButton = tk.Button(self.mainMenu, text='Agregar Insumo', bg='lightgrey', font=('Helvetica', 14), command=self.addIns)
        self.addInsButton.grid(column=0, row=6, pady=5)

        self.mainWindow.mainloop()

    #Funcion para agregar insumos
    def addIns(self):
        from x_home import errorMessage
        nom = self.nomInsEntry.get()
        if nom == '': #Comprobacion de que el campo no este vacio, en caso de estarlo lanza un mensaje de error y recarga la ventana
            errorMessage('Nombre no puede estar vacio')
            self.reload()
        desc = self.descInsEntry.get()
        if desc == '':
            errorMessage('Descripcion no puede estar vacio')
            self.reload()
        med = self.medInsEntry.get() #Este no se confirma porque si puede estar vacio
        can = self.canInsEntry.get()
        if can == '':
            errorMessage('Cantidad no puede estar vacio')
            self.reload()
        canNum = float(can)
        rif = self.rifInsEntry.get()
        if rif == '':
            errorMessage('Rif no puede estar vacio')
            self.reload()
        rifNum = int(rif)
        pre = self.preInsEntry.get()
        if pre == '':
            errorMessage('Precio no puede estar vacio')
            self.reload()
        preNum = float(pre)
        x_func.addIns(nom.capitalize(), desc, med.capitalize(), canNum, rifNum, preNum)
        self.nomInsEntry.delete(0, tk.END)
        self.descInsEntry.delete(0, tk.END)
        self.medInsEntry.delete(0, tk.END)
        self.canInsEntry.delete(0, tk.END)
        self.rifInsEntry.delete(0, tk.END)
        self.preInsEntry.delete(0, tk.END)

    #"Recargar" la ventana
    def reload(self):
        self.mainWindow.destroy()
        win = AddInsumo()
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
        from x_showcliente import ShowCliente
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