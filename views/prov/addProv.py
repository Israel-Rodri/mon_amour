import tkinter as tk
from tkinter import messagebox
from views.prov.baseprov import BaseProvView

#Clase para la vista de agregar proveedor
class AddProvView(BaseProvView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Titulo de la seccion
        self.title = tk.Label(self, text='Agregar Proveedores', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        #Titulo y campo de entrada para rif
        self.rifTitle = tk.Label(self, text='Rif Proveedor:', font=('Helvetica', 14))
        self.rifTitle.grid(column=1, row=1, pady=5, sticky='w')
        vcmdRif = (self.register(self.onValidate), '%P', '9')
        self.rifEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdRif)
        self.rifEntry.grid(column=2, row=1, pady=10, sticky='w')
        self.rifEntry.bind('<KeyRelease>', lambda e: self.verify(self.rifEntry))

        #Titulo y campo de entrada para nombre
        self.nomTitle = tk.Label(self, text='Nombre Proveedor:', font=('Helvetica', 14))
        self.nomTitle.grid(column=1, row=2, pady=5, sticky='w')
        vcmdNom = (self.register(self.onValidate), '%P', '30')
        self.nomEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdNom)
        self.nomEntry.grid(column=2, row=2, pady=10, sticky='w')

        #Titulo y campo de entrada para telefono
        self.telTitle = tk.Label(self, text='Telefono Proveedor:', font=('Helvetica', 14))
        self.telTitle.grid(column=1, row=3, pady=5, sticky='w')
        vcmdTel = (self.register(self.onValidate), '%P', '12')
        self.telEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdTel)
        self.telEntry.grid(column=2, row=3, pady=10, sticky='w')

        #Titulo y campo de entrada para email
        self.emailTitle = tk.Label(self, text='Email Proveedor:', font=('Helvetica', 14))
        self.emailTitle.grid(column=1, row=4, pady=5, sticky='w')
        vcmdEmail = (self.register(self.onValidate), '%P', '25')
        self.emailEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdEmail)
        self.emailEntry.grid(column=2, row=4, pady=10, sticky='w')

        self.addBtn = tk.Button(self, text='Agregar Proveedor', font=('Helvetica', 14), command=lambda: self.addProv(self.rifEntry.get(), self.nomEntry.get(), self.telEntry.get(), self.emailEntry.get()))
        self.addBtn.grid(column=1, row=5, pady=10, sticky='w')

    #Funcion para agregar proveedor con confirmaciones de campos en blanco
    def addProv(self, rif, nom, tel, email):
        if rif == '' or nom == '' or tel == '' or email == '':
            messagebox.showerror('Error', 'De rellenar todos los campos')
        else:
            result = self.controller.insertProv(int(rif), nom, tel, email)
            if result == True:
                messagebox.showinfo('¡Registro Exitoso!', f'El proveedor {nom} ha sido agregado de forma exitosa')
                self.rifEntry.delete(0, tk.END)
                self.nomEntry.delete(0, tk.END)
                self.telEntry.delete(0, tk.END)
                self.emailEntry.delete(0, tk.END)
            else:
                messagebox.showerror('Error', result)
                self.rifEntry.delete(0, tk.END)
                self.nomEntry.delete(0, tk.END)
                self.telEntry.delete(0, tk.END)
                self.emailEntry.delete(0, tk.END)

    #Funcion para limitar la cantidad de caracteres a escribir
    def onValidate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True

    #Funcion para verificar que todos los caracteres sean numericos
    def verify(self, entry):
        code = entry.get()
        for i in code:
            if i not in '0123456789':
                entry.delete(code.index(i), code.index(i)+1)