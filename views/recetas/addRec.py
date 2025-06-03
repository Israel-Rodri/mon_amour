import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from views.recetas.baserec import BaseRecView

#Clase para la vista de agregar proveedor
class AddRecView(BaseRecView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Titulo de la seccion
        self.titleNom = tk.Label(self, text='Agregar Recetas', font=('Helvetica', 18, 'bold'))
        self.titleNom.grid(column=3, row=0, pady=10, sticky='w')

        #Titulo y campo de entrada para nombre
        self.nomTitle = tk.Label(self, text='Nombre Receta:', font=('Helvetica', 14))
        self.nomTitle.grid(column=3, row=1, pady=5, sticky='w')
        vcmdNom = (self.register(self.onValidate), '%P', '20')
        self.nomEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdNom)
        self.nomEntry.grid(column=4, row=1, pady=10, sticky='w')

        #Titulo y campo de entrada de descripcion
        self.descTitle = tk.Label(self, text='Descripción Receta:', font=('Helvetica', 14))
        self.descTitle.grid(column=3, row=2, pady=5, sticky='w')
        vcmdDesc = (self.register(self.onValidate), '%P', '50')
        self.descEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdDesc)
        self.descEntry.grid(column=4, row=2, pady=10, sticky='w')

        #Boton para crear recetas, solo nombre y descripcion
        self.addNomBtn = tk.Button(self, text='Agregar Receta', font=('Helvetica', 14), command=lambda: self.addRecNom(self.nomEntry.get(), self.descEntry.get()))
        self.addNomBtn.grid(column=3, row=3, pady=10, sticky='w')

# -------- Cambio de Seccion --------#

        #Titulo de la seccion
        self.titleIns = tk.Label(self, text='Agregar Insumo a Receta', font=('Helvetica', 18, 'bold'))
        self.titleIns.grid(column=5, row=0, pady=10, sticky='w')

        #Lista desplegable que muestra recetas
        self.nomRecTitle = tk.Label(self, text='Nombre Receta:', font=('Helvetica', 14))
        self.nomRecTitle.grid(column=5, row=1, pady=5, sticky='w')
        self.nomRecCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomRecListVal = []
        self.nomRecList()
        self.nomRecCombo['values'] = self.nomRecListVal
        self.nomRecCombo.current(0)
        self.nomRecCombo.grid(column=6, row=1, pady=5, padx=5, sticky='w')

        #Lista desplegable que muestra insumos
        self.nomInsTitle = tk.Label(self, text='Nombre Insumo:', font=('Helvetica', 14))
        self.nomInsTitle.grid(column=5, row=2, pady=5, sticky='w')
        self.nomInsCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomInsListVal = []
        self.nomInsList()
        self.nomInsCombo['values'] = self.nomInsListVal
        self.nomInsCombo.current(0)
        self.nomInsCombo.grid(column=6, row=2, pady=5, padx=5, sticky='w')

        #Titulo y campo de entrada de cantidad de insumo
        self.canInsTitle = tk.Label(self, text='Cantidad a utilizar del Insumo:', font=('Helvetica', 14))
        self.canInsTitle.grid(column=5, row=3, pady=5, sticky='w')
        vcmdCanIns = (self.register(self.onValidate), '%P', '8')
        self.canInsEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdCanIns)
        self.canInsEntry.grid(column=6, row=3, pady=10, sticky='w')
        self.canInsEntry.bind('<KeyRelease>', lambda e: self.verify(self.canInsEntry))

        #Boton para asociar insumos a recetas
        self.addInsBtn = tk.Button(self, text='Asociar Insumo a Receta', font=('Helvetica', 14), command=lambda: self.addInsRec(self.nomRecCombo.get(), self.nomInsCombo.get(), self.canInsEntry.get()))
        self.addInsBtn.grid(column=5, row=4, pady=10, sticky='w')

    #Funcion para agregar recetas, solo nombre y descripcion
    def addRecNom(self, nom, desc):
        if nom == '' or desc == '':
            messagebox.showerror('Error', 'Debe rellenar todos los campos')
        else:
            result = self.controller.insertRecNom(nom, desc)
            if result == True:
                messagebox.showinfo('¡Registro exitoso!', f'Receta {nom} registrada de forma exitosa')
                self.nomEntry.delete(0, tk.END)
                self.descEntry.delete(0, tk.END)
            else:
                messagebox.showerror('Error', result)
                self.nomEntry.delete(0, tk.END)
                self.descEntry.delete(0, tk.END)

    #Funcion para asociar insumos a recetas
    def addInsRec(self, rec, ins, can):
        if can == '':
            messagebox.showerror('Error', 'Debe rellenar todos los campos')
        else:
            result = self.controller.insertInsRec(rec, ins, float(can))
            if result == True:
                messagebox.showinfo('¡Asociación Exitosa!', f'Insumo {ins} asociado de forma exitosa a la receta {rec}')
                self.canInsEntry.delete(0, tk.END)
            else:
                messagebox.showerror('Error', result)
                self.canInsEntry.delete(0, tk.END)

    #Funcion para mostrar insumos en una lista desplegable
    def nomInsList(self):
        nomList = self.controller.nomInsList()
        for i in nomList:
            self.nomInsListVal.append(i[0])

    #Funcion para mostrar recetas en una lista desplegable
    def nomRecList(self):
        nomList = self.controller.nomRecList()
        for i in nomList:
            self.nomRecListVal.append(i[0])

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