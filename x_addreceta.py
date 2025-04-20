import tkinter as tk
import x_func

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
        from x_home import errorMessage
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
        from x_home import errorMessage
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
        from x_home import errorMessage
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
        from x_showcliente import ShowCliente
        self.mainWindow.destroy()
        win = ShowCliente()
        win

    def addRecButton(self):
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