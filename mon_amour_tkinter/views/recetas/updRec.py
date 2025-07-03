import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from views.recetas.baserec import BaseRecView

#Clase para la vista de agregar proveedor
class UpdRecView(BaseRecView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self. controller = controller

        #Titulo de la seccion
        self.titleNom = tk.Label(self, text='Actualizar Recetas', font=('Helvetica', 18, 'bold'))
        self.titleNom.grid(column=1, row=0, pady=10, sticky='w')

        #Lista desplegable para mostrar recetas
        self.nomRecTitle = tk.Label(self, text='Nombre Receta:', font=('Helvetica', 14))
        self.nomRecTitle.grid(column=1, row=1, pady=5, sticky='w')
        self.nomRecCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomRecListVal = []
        self.nomRecList()
        self.nomRecCombo['values'] = self.nomRecListVal
        self.nomRecCombo.current(0)
        self.nomRecCombo.grid(column=2, row=1, pady=5, padx=5, sticky='w')

        #Titulo y campo de entrada de cantidad de recetas a agregar
        self.canTitle = tk.Label(self, text='Cantidad a Agregar:', font=('Helvetica', 14))
        self.canTitle.grid(column=1, row=2, pady=5, sticky='w')
        vcmdCan =(self.register(self.onValidate), '%P', 8)
        self.canEntry = tk.Spinbox(self, from_=0, to=500, increment=1, font=('Helvetica', 14), validate='key', validatecommand=vcmdCan)
        self.canEntry.grid(column=2, row=2, pady=5, padx=5, sticky='w') 
        self.canEntry.bind('<KeyRelease>', lambda e: self.verify(self.canEntry))

        #Boton para actualizar la cantidad de las recetas
        self.addNomBtn = tk.Button(self, text='Actualizar Cantidad de Receta', font=('Helvetica', 14), command=lambda: self.updCanRec(self.nomRecCombo.get(), self.canEntry.get()))
        self.addNomBtn.grid(column=1, row=3, pady=10, sticky='w')

    def updCanRec(self, rec, can):
        if can == '' or can == '0':
            messagebox.showerror('Error', 'La cantidad a agregar no puede estar vacía ni ser igual a 0')
        else:
            result = self.controller.updCanRec(rec, int(can))
            if result == True:
                messagebox.showinfo('¡Actualización exitosa!', f'Cantidad de la receta {rec} actualizada de forma exitosa')
            else:
                messagebox.showerror('Error', result)

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