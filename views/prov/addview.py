import tkinter as tk
from tkinter import messagebox
from views.prov.mainview import View

class AddView(View):
    def __init__ (self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry('800x600')

        """self.provMenu = tk.Menu(self.root)

        self.provMenuOptions = tk.Menu(self.provMenu, tearoff=0)
        self.provMenuOptions.add_command(label='Mostrar')
        self.provMenuOptions.add_command(label='Agregar')
        self.provMenuOptions.add_command(label='Actualizar')
        self.provMenuOptions.add_command(label='Eliminar')

        self.provMenu.add_cascade(label='Proveedores', menu=self.provMenuOptions)

        self.root.config(menu=self.provMenu)"""
        self.provRifLabel = tk.Label(self.root, text='Rif:', font=('Helvetica', 16))
        self.provRifLabel.grid(column=0, row=0, padx=5)
        vcmdRif = (self.register(self.validate), '%P', '10')
        self.provRifEntry = tk.Entry(self.root, validate='key', validatecommand=vcmdRif, font=('Helvetica', 16))
        self.provRifEntry.grid(column=1, row=0, padx=5)
        self.provRifEntry.bind('<KeyRelease>', lambda e: self.validateRif())

        self.provNomLabel = tk.Label(self.root, text='Nombre:', font=('Helvetica', 16))
        self.provNomLabel.grid(column=0, row=1, padx=5)
        vcmdNom = (self.register(self.validate), '%P', '30')
        self.provNomEntry = tk.Entry(self.root, validate='key', validatecommand=vcmdNom, font=('Helvetica', 16))
        self.provNomEntry.grid(column=1, row=1, padx=5)

        self.provTelLabel = tk.Label(self.root, text='Telefono:', font=('Helvetica', 16))
        self.provTelLabel.grid(column=0, row=2, padx=5)
        vcmdTel = (self.register(self.validate), '%P', '12')
        self.provTelEntry = tk.Entry(self.root, validate='key', validatecommand=vcmdTel, font=('Helvetica', 16))
        self.provTelEntry.grid(column=1, row=2, padx=5)
        self.provTelEntry.bind('<KeyRelease>', lambda e: self.validateTel())

        self.provEmailLabel = tk.Label(self.root, text='Email:', font=('Helvetica', 16))
        self.provEmailLabel.grid(column=0, row=3, padx=5)
        vcmdEmail = (self.register(self.validate), '%P', '25')
        self.provEmailEntry = tk.Entry(self.root, validate='key', validatecommand=vcmdEmail, font=('Helvetica', 16))
        self.provEmailEntry.grid(column=1, row=3, padx=5)

        self.provInsertBtn = tk.Button(self.root, text='Agregar Proveedor', font=('Helvetica', 16), command=lambda:self.clickInsert(self.provRifEntry.get(), self.provNomEntry.get(), self.provTelEntry.get(), self.provEmailEntry.get()))
        self.provInsertBtn.grid(column=0, row=4, padx=5)

    def set_controller(self, controller):
        self.controller = controller

    def clickInsert(self, rif, nom, tel, email):
        if rif == '' or nom == '' or tel == '' or email == '':
            messagebox.showerror('Error', 'Debe rellenar todos los campos')
        else:
            rifNum = int(rif)
            result = self.controller.insertar(rifNum, nom, tel, email)
            if result != True:
                messagebox.showerror('Error', result)
                self.provRifEntry.delete(0, tk.END)
                self.provNomEntry.delete(0, tk.END)
                self.provTelEntry.delete(0, tk.END)
                self.provEmailEntry.delete(0, tk.END)
            else:
                messagebox.showinfo('Estado', f'Proveedor {nom} registrado de forma exitosa')

    def validate(self, word, length):
        if len(word) > int(length):
            self.bell()
            return False
        return True

    def validateTel(self):
        number = self.provTelEntry.get()
        for i in number:
            if i not in '0123456789-':
                self.provTelEntry.delete(number.index(i), number.index(i)+1)

    def validateRif(self):
        rif = self.provRifEntry.get()
        for i in rif:
            if i not in '0123456789-':
                self.provRifEntry.delete(rif.index(i), rif.index(i)+1)