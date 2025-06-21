import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.prov.baseprov import BaseProvView

class UpdProvView(BaseProvView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        #Titulo de la seccion
        self.title = tk.Label(self, text='Actualizar Proveedor', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        #Lista desplegable que muestra insumos
        self.nomProvTitle = tk.Label(self, text='Nombre Proveedor:', font=('Helvetica', 14))
        self.nomProvTitle.grid(column=2, row=1, pady=5, sticky='w')
        self.nomProvCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomProvListVal = []
        self.nomProvList()
        self.nomProvCombo['values'] = self.nomProvListVal
        self.nomProvCombo.current(0)
        self.nomProvCombo.grid(column=3, row=1, pady=5, padx=5, sticky='w')

        #nombre, tel, email
        #Titulo y campo de entrada para nombre
        self.nomTitle = tk.Label(self, text='Nombre Proveedor:', font=('Helvetica', 14))
        self.nomTitle.grid(column=2, row=2, pady=5, sticky='w')
        vcmdNom = (self.register(self.onValidate), '%P', '30')
        self.nomEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdNom)
        self.nomEntry.grid(column=3, row=2, pady=10, sticky='w')
        self.nomEntry.bind('<KeyRelease>', lambda e: self.verifyLetter(self.nomEntry))

        #Titulo y campo de entrada para telefono
        self.telTitle = tk.Label(self, text='Teléfono Proveedor:', font=('Helvetica', 14))
        self.telTitle.grid(column=2, row=3, pady=5, sticky='w')
        vcmdTel = (self.register(self.onValidate), '%P', '12')
        self.telEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdTel)
        self.telEntry.grid(column=3, row=3, pady=10, sticky='w')
        self.telEntry.bind('<KeyRelease>', lambda e: self.verifyTel(self.telEntry))

        #Titulo y campo de entrada para nombre
        self.emailTitle = tk.Label(self, text='Correo Proveedor:', font=('Helvetica', 14))
        self.emailTitle.grid(column=2, row=4, pady=5, sticky='w')
        vcmdEmail = (self.register(self.onValidate), '%P', '35')
        self.emailEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdEmail)
        self.emailEntry.grid(column=3, row=4, pady=10, sticky='w')

        #Boton para asociar insumos a recetas
        self.addProvBtn = tk.Button(self, text='Actualizar Proveedor', font=('Helvetica', 14), command=lambda: self.updProv(self.nomProvCombo.get(), self.nomEntry.get(), self.telEntry.get(), self.emailEntry.get()))
        self.addProvBtn.grid(column=2, row=5, pady=10, sticky='w')

    def updProv(self, nomAct, nom, tel, email):
        if email != '':
            emailCorr = self.verifyEmail(email)
        else:
            emailCorr = ''
        result = self.controller.updProv(nomAct, nom, tel, emailCorr)
        if result == True:
            messagebox.showinfo('¡Actualización exitosa!', 'Proveedor actualizado de forma exitosa')
            self.nomEntry.delete(0, tk.END)
            self.telEntry.delete(0, tk.END)
            self.emailEntry.delete(0, tk.END)
        else:
            messagebox.showerror('Error', result)
            self.nomEntry.delete(0, tk.END)
            self.telEntry.delete(0, tk.END)
            self.emailEntry.delete(0, tk.END)

    def nomProvList(self):
        nomList = self.controller.nomProvList()
        for i in nomList:
            self.nomProvListVal.append(i[0])

    #Funcion para limitar la cantidad de caracteres a escribir
    def onValidate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True

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