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
        vcmdRif = (self.register(self.onValidate), '%P', '10')
        self.rifEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdRif)
        self.rifEntry.grid(column=2, row=1, pady=10, sticky='w')
        self.rifEntry.bind('<KeyRelease>', lambda e: self.verifyRif(self.rifEntry))

        #Titulo y campo de entrada para nombre
        self.nomTitle = tk.Label(self, text='Nombre Proveedor:', font=('Helvetica', 14))
        self.nomTitle.grid(column=1, row=2, pady=5, sticky='w')
        vcmdNom = (self.register(self.onValidate), '%P', '30')
        self.nomEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdNom)
        self.nomEntry.grid(column=2, row=2, pady=10, sticky='w')
        self.nomEntry.bind('<KeyRelease>', lambda e: self.verifyLetter(self.nomEntry))

        #Titulo y campo de entrada para telefono
        self.telTitle = tk.Label(self, text='Telefono Proveedor:', font=('Helvetica', 14))
        self.telTitle.grid(column=1, row=3, pady=5, sticky='w')
        vcmdTel = (self.register(self.onValidate), '%P', '12')
        self.telEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdTel)
        self.telEntry.grid(column=2, row=3, pady=10, sticky='w')
        self.telEntry.bind('<KeyRelease>', lambda e: self.verifyTel(self.telEntry))

        #Titulo y campo de entrada para email
        self.emailTitle = tk.Label(self, text='Email Proveedor:', font=('Helvetica', 14))
        self.emailTitle.grid(column=1, row=4, pady=5, sticky='w')
        vcmdEmail = (self.register(self.onValidate), '%P', '35')
        self.emailEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdEmail)
        self.emailEntry.grid(column=2, row=4, pady=10, sticky='w')

        self.addBtn = tk.Button(self, text='Agregar Proveedor', font=('Helvetica', 14), command=lambda: self.addProv(self.rifEntry.get(), self.nomEntry.get(), self.telEntry.get(), self.emailEntry.get()))
        self.addBtn.grid(column=1, row=5, pady=10, sticky='w')

    #Funcion para agregar proveedor con confirmaciones de campos en blanco
    def addProv(self, rif, nom, tel, email):
        if rif == '' or nom == '':
            messagebox.showerror('Error', 'Debe rellenar todos los campos')
        else:
            if email:
                emailCorr = self.verifyEmail(email)
            else:
                emailCorr = ''
            result = self.controller.insertProv(rif, nom, tel, emailCorr)
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
    def verifyRif(self, entry):
        code = entry.get()
        for i in code:
            if i not in '0123456789vVjJcC':
                entry.delete(code.index(i), code.index(i)+1)

    #Funcion para verificar que todos los caracteres no sean numericos
    def verifyLetter(self, entry):
        code = entry.get()
        for i in code:
            if i in '0123456789':
                entry.delete(code.index(i), code.index(i)+1)

    #Funcion para verificar que todos los caracteres sean numericos o guion
    def verifyTel(self, entry):
        code = entry.get()
        for i in code:
            if i not in '0123456789-':
                entry.delete(code.index(i), code.index(i)+1)

    def verifyEmail(self, entry):
        entrySplit = entry.split('@')
        if len(entrySplit) == 2:
            if ' ' or '@' not in entrySplit[0]:
                domCorreo = entrySplit[1].split('.')
                if '_' or '-' or ',' not in domCorreo[0] and 'com' in domCorreo[1]:
                    return entry
                else:
                    pass
            else:
                messagebox.showerror('Error', f'Formato de correo inválido\nDebe estar en formato "usuario@correo.com"\nCorreo suministrado: {entry}')
        else:
            messagebox.showerror('Error', f'Formato de correo inválido\nDebe estar en formato "usuario@correo.com"\nCorreo suministrado: {entry}')