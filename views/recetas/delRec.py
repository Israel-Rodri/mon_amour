import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.recetas.baserec import BaseRecView

class DelRecView(BaseRecView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        # Título de la sección
        self.title = tk.Label(self, text='Eliminar Receta', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        # Lista desplegable de recetas
        self.nomRecTitle = tk.Label(self, text='Nombre Receta:', font=('Helvetica', 14))
        self.nomRecTitle.grid(column=2, row=1, pady=5, sticky='w')
        self.nomRecCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomRecListVal = []
        self.nomRecList()
        self.nomRecCombo['values'] = self.nomRecListVal
        if self.nomRecListVal:
            self.nomRecCombo.current(0)
        self.nomRecCombo.grid(column=3, row=1, pady=5, padx=5, sticky='w')

        # Botón para eliminar receta
        self.delRecBtn = tk.Button(
            self,
            text='Eliminar receta',
            font=('Helvetica', 14),
            command=self.delRec
        )
        self.delRecBtn.grid(column=2, row=2, pady=10, sticky='w')

    def nomRecList(self):
        nomList = self.controller.nomRecList()
        self.nomRecListVal.clear()
        for i in nomList:
            self.nomRecListVal.append(i[0])

    def delRec(self):
        nom = self.nomRecCombo.get()
        if not nom:
            messagebox.showerror('Error', 'Seleccione una receta para eliminar')
            return

        # Ventana de confirmación personalizada
        confirm = tk.Toplevel(self)
        confirm.title("Confirmar eliminación")
        confirm.geometry("430x120")
        confirm.resizable(False, False)
        tk.Label(confirm, text=f"¿Está seguro que desea eliminar\nla receta '{nom}'?", font=('Helvetica', 12)).pack(pady=10)

        btn_frame = tk.Frame(confirm)
        btn_frame.pack(pady=10)

        def confirmar():
            result = self.controller.delRec(nom)
            if result == True:
                messagebox.showinfo('¡Eliminación exitosa!', 'Receta eliminada de forma exitosa')
                self.nomRecList()
                self.nomRecCombo['values'] = self.nomRecListVal
                if self.nomRecListVal:
                    self.nomRecCombo.current(0)
                else:
                    self.nomRecCombo.set('')
            else:
                messagebox.showerror('Error', result)
            confirm.destroy()

        def cancelar():
            confirm.destroy()

        tk.Button(btn_frame, text="Sí", font=('Helvetica', 12), width=8, command=confirmar).pack(side='left', padx=10)
        tk.Button(btn_frame, text="No", font=('Helvetica', 12), width=8, command=cancelar).pack(side='right', padx=10)

        confirm.transient(self)
        confirm.grab_set()
        self.wait_window(confirm)