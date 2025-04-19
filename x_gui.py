import tkinter as tk
from tkinter import messagebox
import x_func #Importa las funciones del CRUD

#Menu de inicio xq se ve muy feo iniciar en una funcion
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
        win = ShowCliente()
        win

    def addProvButton(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para crear la ventana de agregar proveedor
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para mostrar los proveedores
class ShowProveedor:
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

        self.rifLabel = tk.Label(self.mainMenu, text='Rif', bg='white', font=('Helvetica', 16))
        self.rifLabel.grid(column=0, row=0, padx=10, pady=5)

        self.nomLabel = tk.Label(self.mainMenu, text='Nombre', bg='white', font=('Helvetica', 16))
        self.nomLabel.grid(column=1, row=0, padx=10, pady=5)
        
        self.telLabel = tk.Label(self.mainMenu, text='Telefono', bg='white', font=('Helvetica', 16))
        self.telLabel.grid(column=2, row=0, padx=10, pady=5)

        self.emailLabel = tk.Label(self.mainMenu, text='Email', bg='white', font=('Helvetica', 16))
        self.emailLabel.grid(column=3, row=0, padx=10, pady=5)

        #Invocacion de la funcion para mostrar
        self.showProv()

        self.mainWindow.mainloop()

    #Funcion para mostrar los proveedores
    def showProv(self):
        prov = x_func.showProv() #Invocacion del CRUD para mostrar
        variables = [] #Creacion de una lista de variables para poder mostrar, NO TOCAAAAAAAAAR
        r = 1 #Variable de control
        for i in range(len(prov)): #Bucle para poder mostrar todos los proveedores independientemente de la cantidad
            col = 0
            for j in prov[i]:
                variables.append(col)
                variables[col] = tk.Label(self.mainMenu, text=j, bg='white', font=('Helvetica', 16))
                variables[col].grid(column=col, row=r, padx=10, pady=5)
                col += 1
            r += 1

    #Funcion para "recargar"
    def reload(self):
        self.mainWindow.destroy()
        win = ShowProveedor()
        win

    def addProvButton(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para agregar insumo
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
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para mostrar todos los insumos
class ShowInsumo:
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

        self.nomLabel = tk.Label(self.mainMenu, text='Nombre', bg='white', font=('Helvetica', 16))
        self.nomLabel.grid(column=0, row=0, padx=10, pady=5)

        self.descLabel = tk.Label(self.mainMenu, text='Descripcion', bg='white', font=('Helvetica', 16))
        self.descLabel.grid(column=1, row=0, padx=10, pady=5)

        self.medLabel = tk.Label(self.mainMenu, text='Unidad de Medida', bg='white', font=('Helvetica', 16))
        self.medLabel.grid(column=2, row=0, padx=10, pady=5)

        self.canLabel = tk.Label(self.mainMenu, text='Cantidad', bg='white', font=('Helvetica', 16))
        self.canLabel.grid(column=3, row=0, padx=10, pady=5)

        self.preLabel = tk.Label(self.mainMenu, text='Precio Unitario', bg='white', font=('Helvetica', 16))
        self.preLabel.grid(column=4, row=0, padx=10, pady=5)

        #Llamado a la funcion para mostrar los insumos
        self.showIns()

        self.mainWindow.mainloop()

    #Funcion para llamar a los insumos
    def showIns(self):
        ins = x_func.showIns() #CRUD para leer los insumos
        variables = [] #Variables de control
        r = 1
        for i in range(len(ins)): #Bucle para mostrar todos los insumos independientemente de la cantida, NO TOCAAAAAAAAAAAAR
            col = 0
            for j in ins[i]:
                variables.append(col)
                if col != 0 and col != 5:
                    if col < 6:
                        variables[col] = tk.Label(self.mainMenu, text=j, bg='white', font=('Helvetica', 16))
                        variables[col].grid(column=col-1, row=r, padx=10, pady=5)
                    elif col > 5:
                        variables[col] = tk.Label(self.mainMenu, text=j, bg='white', font=('Helvetica', 16))
                        variables[col].grid(column=col-2, row=r, padx=10, pady=5)
                elif col == 0 or col == 5: pass
                col += 1
            r += 1

    #"Recargar" la ventana
    def reload(self):
        self.mainWindow.destroy()
        win = ShowInsumo()
        win

    def addProvButton(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para agregar clientes
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
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para mostrar los clientes
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
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Clase para agregar recetas, por ahora solo nombre y descripcion
class AddReceta:
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

        self.nomRecLabel = tk.Label(self.mainMenu, text='Nombre:', bg='white', font=('Helvetica', 16))
        self.nomRecLabel.grid(column=0, row=0, padx=10, pady=5)
        self.nomRecEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.nomRecEntry.grid(column=1, row=0, pady=5)

        self.descRecLabel = tk.Label(self.mainMenu, text='Breve descripcion:', bg='white', font=('Helvetica', 16))
        self.descRecLabel.grid(column=0, row=1, padx=10, pady=5)
        self.descRecEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.descRecEntry.grid(column=1, row=1, pady=5)

        self.addCRecButton = tk.Button(self.mainMenu, text='Agregar Receta', bg='lightgrey', font=('Helvetica', 14), command=self.addRec)
        self.addCRecButton.grid(column=0, row=2, pady=5)

        self.blank = tk.Label(self.mainMenu, text='', bg='white').grid(column=0, row=3)

        self.insUtRecLabel = tk.Label(self.mainMenu, text='Insumo a utilizar:', bg='white', font=('Helvetica', 16))
        self.insUtRecLabel.grid(column=0, row=4, padx=10, pady=5)
        self.insUtRecEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.insUtRecEntry.grid(column=1, row=4, pady=5)

        self.canUtRecLabel = tk.Label(self.mainMenu, text='Cantidad del insumo a utilizar:', bg='white', font=('Helvetica', 16))
        self.canUtRecLabel.grid(column=0, row=5, padx=10, pady=5)
        self.canUtRecEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.canUtRecEntry.grid(column=1, row=5, pady=5)

        self.recUtInsLabel = tk.Label(self.mainMenu, text='Receta:', bg='white', font=('Helvetica', 16))
        self.recUtInsLabel.grid(column=0, row=6, padx=10, pady=5)
        self.recUtInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.recUtInsEntry.grid(column=1, row=6, pady=5)

        self.addCRecButton = tk.Button(self.mainMenu, text='Agregar Insumos a Utilizar', bg='lightgrey', font=('Helvetica', 14), command=self.addInsRec)
        self.addCRecButton.grid(column=0, row=7, pady=5)

        self.recConNomLabel = tk.Label(self.mainMenu, text='Nombre receta:', bg='white', font=('Helvetica', 16))
        self.recConNomLabel.grid(column=0, row=8, padx=10, pady=5)
        self.recConNomEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.recConNomEntry.grid(column=1, row=8, pady=5)
        
        self.recConLabel = tk.Label(self.mainMenu, text='Cantidad receta:', bg='white', font=('Helvetica', 16))
        self.recConLabel.grid(column=0, row=9, padx=10, pady=5)
        self.recCon = tk.Spinbox(self.mainMenu, from_=0, to=100, increment=1, font=('Helvetica', 14), bg='white')
        self.recCon.config(state='normal', justify='center', wrap=True)
        self.recCon.grid(column=1, row=9, padx=10, pady=5)

        self.RecButton = tk.Button(self.mainMenu, text='Aumentar cantidad de receta', bg='lightgrey', font=('Helvetica', 14), command=self.updateCanRec)
        self.RecButton.grid(column=0, row=10, pady=5)

        self.mainWindow.mainloop()

    def addRec(self):
        nom = self.nomRecEntry.get()
        if nom == '':
            errorMessage('Nombre de la receta no puede estar vacio')
            self.reload()
        desc = self.descRecEntry.get()
        if desc == '':
            errorMessage('Descripcion de la receta no puede estar vacia')
            self.reload()
        x_func.addRec(nom.capitalize(), desc)
        self.nomRecEntry.delete(0, tk.END)
        self.descRecEntry.delete(0, tk.END)

    def addInsRec(self):
        ins = self.insUtRecEntry.get()
        if ins == '':
            errorMessage('Insumo no puede estar vacio')
            self.reload()
        can = self.canUtRecEntry.get()
        if can == '' or can == '0':
            errorMessage('Cantidad no puede estar vacio ni puede valer 0')
            self.reload()
        canNum = float(can)
        rec = self.recUtInsEntry.get()
        if rec == '':
            errorMessage('Receta no puede estar vacia')
            self.reload()
        x_func.addInsRec(rec.capitalize(), ins.capitalize(), canNum)
        self.insUtRecEntry.delete(0, tk.END)
        self.canUtRecEntry.delete(0, tk.END)
        self.recUtInsEntry.delete(0, tk.END)

    def updateCanRec(self):
        recConNom = self.recConNomEntry.get()
        if recConNom == '':
            errorMessage('Nombre de receta no puede estar vacío')
            self.reload()
        recCon = self.recCon.get()
        if recCon == '0':
            errorMessage('La cantidad a actualizar no puede ser 0')
            self.reload()
        recConNum = int(recCon)
        x_func.updateCanRec(recConNom.capitalize(), recConNum)
        self.recConNomEntry.delete(0, tk.END)

    def reload(self):
        self.mainWindow.destroy()
        win = AddReceta()
        win

    def addProvButton(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

class UpdateInsumo:
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

        self.nomInsLabel = tk.Label(self.mainMenu, text='Nombre:', bg='white', font=('Helvetica', 16))
        self.nomInsLabel.grid(column=0, row=0, padx=10, pady=5)
        self.nomInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.nomInsEntry.grid(column=1, row=0, pady=5)

        self.canInsLabel = tk.Label(self.mainMenu, text='Cantidad a agregar:', bg='white', font=('Helvetica', 16))
        self.canInsLabel.grid(column=0, row=1, padx=10, pady=5)
        self.canInsEntry = tk.Entry(self.mainMenu, bg='white', font=('Helvetica', 16))
        self.canInsEntry.grid(column=1, row=1, pady=5)

        self.updateButton = tk.Button(self.mainMenu, text='Aumentar cantidad de receta', bg='lightgrey', font=('Helvetica', 14), command=self.updateCanIns)
        self.updateButton.grid(column=0, row=2, pady=5)

        self.mainWindow.mainloop()

    def updateCanIns(self):
        nom = self.nomInsEntry.get()
        if nom == '':
            errorMessage('Nombre no puede estar vacío')
            self.reload()
        can = self.canInsEntry.get()
        if can == '':
            errorMessage('Cantidad no puede estar vacío')
            self.reload()
        canNum = float(can)
        x_func.updateCanIns(nom.capitalize(), canNum)
        self.nomInsEntry.delete(0, tk.END)
        self.canInsEntry.delete(0, tk.END)

    def reload(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def addProvButton(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

class ShowReceta:
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

        self.nomLabel = tk.Label(self.mainMenu, text='Nombre', bg='white', font=('Helvetica', 16))
        self.nomLabel.grid(column=0, row=0, padx=10, pady=5)

        self.descLabel = tk.Label(self.mainMenu, text='Descripcion', bg='white', font=('Helvetica', 16))
        self.descLabel.grid(column=1, row=0, padx=10, pady=5)

        self.canLabel = tk.Label(self.mainMenu, text='Cantidad', bg='white', font=('Helvetica', 16))
        self.canLabel.grid(column=2, row=0, padx=10, pady=5)

        self.preLabel = tk.Label(self.mainMenu, text='Precio', bg='white', font=('Helvetica', 16))
        self.preLabel.grid(column=3, row=0, padx=10, pady=5)

        self.showRec()

        self.mainWindow.mainloop()

    def showRec(self):
        rec = x_func.showRec() #CRUD para leer los insumos
        variables = [] #Variables de control
        r = 1
        for i in range(len(rec)): #Bucle para mostrar todos los insumos independientemente de la cantida, NO TOCAAAAAAAAAAAAR
            col = 0
            for j in rec[i]:
                variables.append(col)
                if col != 0:
                        variables[col] = tk.Label(self.mainMenu, text=j, bg='white', font=('Helvetica', 16))
                        variables[col].grid(column=col-1, row=r, padx=10, pady=5)
                elif col == 0: pass
                col += 1
            r += 1

    def reload(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

    def addProvButton(self):
        self.mainWindow.destroy()
        win = AddProveedor()
        win

    def showProvButton(self):
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
        win = AddCliente()
        win

    def showCliButton(self):
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
        self.mainWindow.destroy()
        win = AddCliente()
        win

    def updateInsButton(self):
        self.mainWindow.destroy()
        win = UpdateInsumo()
        win

    def showRecButton(self):
        self.mainWindow.destroy()
        win = ShowReceta()
        win

#Crea una ventana emergente de error, recibe como parametro un mensaje para mostrar
def errorMessage(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Ocurrio un error', message)

#Ejecucion de la primera clase, puede ser la que sea
#messagebox.showinfo('Agregar Recetas', 'Crear las funciones para que se descuente la cantidad de insumos al agregar recetas, tambien modificar la bd para almacenar el precio de las recetas porque creo que eso no esta')
win = Home()
win