import tkinter as tk
import x_func

class AddProveedor:
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

        self.rifProvLabel = tk.Label(self.mainMenu, text='Rif del proveedor:', bg='white', font=('Helvetica', 18))
        self.rifProvLabel.grid(column=0, row=0, pady=5)
        self.rifProvEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.rifProvEntry.grid(column=1, row=0,pady=5)

        self.nomProvLabel = tk.Label(self.mainMenu, text='Nombre del proveedor:', bg='white', font=('Helvetica', 18))
        self.nomProvLabel.grid(column=0, row=1, pady=5)
        self.nomProvEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.nomProvEntry.grid(column=1, row=1, pady=5)

        self.telProvLabel = tk.Label(self.mainMenu, text='Telefono del proveedor:', bg='white', font=('Helvetica', 18))
        self.telProvLabel.grid(column=0, row=2, pady=5)
        self.telProvEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.telProvEntry.grid(column=1, row=2, pady=5)

        self.emailProvLabel = tk.Label(self.mainMenu, text='Email del proveedor:', bg='white', font=('Helvetica', 18))
        self.emailProvLabel.grid(column=0, row=3, pady=5)
        self.emailProvEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.emailProvEntry.grid(column=1, row=3, pady=5)

        self.addProvButton = tk.Button(self.mainMenu, text='Agregar Proveedor', bg='lightgrey', font=('Helvetica', 14), command=self.addProv)
        self.addProvButton.grid(column=0, row=4, pady=5)
        
        self.mainWindow.mainloop()

    #Funcion para agregar proveedor
    def addProv(self):
        from x_home import errorMessage
        rif = self.rifProvEntry.get()
        if rif == '': #Confirmacion de que el campo no se envie vacio, si esta vacio da un mensaje de error y recarga la ventana
            errorMessage('Rif no puede estar vacio')
            self.reload()
        rifNum = int(rif)
        nom = self.nomProvEntry.get()
        if nom == '':
            errorMessage('Nombre no puede estar vacio')
            self.reload()
        tel = self.telProvEntry.get()
        if tel == '':
            errorMessage('Telefono no puede estar vacio')
            self.reload()
        email = self.emailProvEntry.get()
        x_func.addProv(rifNum, nom, tel, email) #Invocaion del CRUD
        self.rifProvEntry.delete(0, tk.END) #Borra los datos escritos en los campos de entrada de texto
        self.nomProvEntry.delete(0, tk.END)
        self.telProvEntry.delete(0, tk.END)
        self.emailProvEntry.delete(0, tk.END)

    #Funcion para "recargar" la ventana, destruye y vuelve a invocar la ventana
    def reload(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def addProvButton(self):
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