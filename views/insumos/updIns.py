import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.insumos.baseins import BaseInsView

#Clase para mostrar los insumos
class UpdInsView(BaseInsView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Titulo de la seccion
        self.title = tk.Label(self, text='Actualizar Insumos', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        #Lista desplegable que muestra insumos
        self.nomInsTitle = tk.Label(self, text='Nombre Insumo:', font=('Helvetica', 14))
        self.nomInsTitle.grid(column=2, row=1, pady=5, sticky='w')
        self.nomInsCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomInsListVal = []
        self.nomInsList()
        self.nomInsCombo['values'] = self.nomInsListVal
        self.nomInsCombo.current(0)
        self.nomInsCombo.grid(column=3, row=1, pady=5, padx=5, sticky='w')

        #nombre, descripcion, medida, cantidad, rif, pre

        #Titulo y campo de entrada para nombre
        self.nomTitle = tk.Label(self, text='Nombre Insumo:', font=('Helvetica', 14))
        self.nomTitle.grid(column=2, row=2, pady=5, sticky='w')
        vcmdNom = (self.register(self.onValidate), '%P', '25')
        self.nomEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdNom)
        self.nomEntry.grid(column=3, row=2, pady=10, sticky='w')

        #Titulo y campo de entrada para descripcion
        self.descTitle = tk.Label(self, text='Descripción Insumo:', font=('Helvetica', 14))
        self.descTitle.grid(column=2, row=3, pady=5, sticky='w')
        vcmdDesc = (self.register(self.onValidate), '%P', '50')
        self.descEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdDesc)
        self.descEntry.grid(column=3, row=3, pady=10, sticky='w')

        #Titulo y campo de entrada para medida
        self.medTitle = tk.Label(self, text='Unidad de Medida Insumo:', font=('Helvetica', 14))
        self.medTitle.grid(column=2, row=4, pady=5, sticky='w')
        vcmdMed = (self.register(self.onValidate), '%P', '10')
        self.medEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdMed)
        self.medEntry.grid(column=3, row=4, pady=10, sticky='w')

        #Titulo y campo de entrada para cantidad
        self.canTitle = tk.Label(self, text='Cantidad Insumo:', font=('Helvetica', 14))
        self.canTitle.grid(column=2, row=5, pady=5, sticky='w')
        vcmdCan = (self.register(self.onValidate), '%P', '8')
        self.canEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdCan)
        self.canEntry.grid(column=3, row=5, pady=10, sticky='w')
        self.canEntry.bind('<KeyRelease>', lambda e: self.verify(self.canEntry))

        #Titulo y campo de entrada para precio
        self.preTitle = tk.Label(self, text='Precio Insumo:', font=('Helvetica', 14))
        self.preTitle.grid(column=2, row=6, pady=5, sticky='w')
        vcmdPre = (self.register(self.onValidate), '%P', '8')
        self.preEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdPre)
        self.preEntry.grid(column=3, row=6, pady=10, sticky='w')
        self.preEntry.bind('<KeyRelease>', lambda e: self.verify(self.preEntry))

        #Boton para asociar insumos a recetas
        self.addInsBtn = tk.Button(self, text='Actualizar Insumo', font=('Helvetica', 14), command=lambda: self.updIns(self.nomInsCombo.get(), self.nomEntry.get(), self.descEntry.get(), self.medEntry.get(), self.canEntry.get(), self.preEntry.get()))
        self.addInsBtn.grid(column=2, row=7, pady=10, sticky='w')

    def updIns(self, ins, nom, desc, med, can, pre):
        result = self.controller.updIns(ins, nom, desc, med.capitalize(), can, pre)
        if result == True:
            messagebox.showinfo('¡Actualización exitosa!', 'Insumo actualizado de forma exitosa')
            self.nomEntry.delete(0, tk.END)
            self.descEntry.delete(0, tk.END)
            self.medEntry.delete(0, tk.END)
            self.canEntry.delete(0, tk.END)
            self.preEntry.delete(0, tk.END)
        else:
            messagebox.showerror('Error', result)
            self.nomEntry.delete(0, tk.END)
            self.descEntry.delete(0, tk.END)
            self.medEntry.delete(0, tk.END)
            self.canEntry.delete(0, tk.END)
            self.preEntry.delete(0, tk.END)

    #Funcion para mostrar insumos en una lista desplegable
    def nomInsList(self):
        nomList = self.controller.nomInsList()
        for i in nomList:
            self.nomInsListVal.append(i[0])

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
            if i not in '0123456789.':
                entry.delete(code.index(i), code.index(i)+1)