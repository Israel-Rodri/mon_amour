import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.insumos.baseins import BaseInsView

class DelInsView(BaseInsView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        # Título de la sección
        self.title = tk.Label(self, text='Eliminar Insumo', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        # Lista desplegable de insumos
        self.nomInsTitle = tk.Label(self, text='Nombre Insumo:', font=('Helvetica', 14))
        self.nomInsTitle.grid(column=2, row=1, pady=5, sticky='w')
        self.nomInsCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomInsListVal = []
        self.nomInsList()
        self.nomInsCombo['values'] = self.nomInsListVal
        if self.nomInsListVal:
            self.nomInsCombo.current(0)
        self.nomInsCombo.grid(column=3, row=1, pady=5, padx=5, sticky='w')

        # Botón para eliminar insumo
        self.delInsBtn = tk.Button(
            self,
            text='Eliminar insumo',
            font=('Helvetica', 14),
            command=self.delIns
        )
        self.delInsBtn.grid(column=2, row=2, pady=10, sticky='w')

    def nomInsList(self):
        nomList = self.controller.nomInsList()
        self.nomInsListVal.clear()
        for i in nomList:
            self.nomInsListVal.append(i[0])

    def delIns(self):
        nom = self.nomInsCombo.get()
        if not nom:
            messagebox.showerror('Error', 'Seleccione un insumo para eliminar')
            return

        # Ventana de confirmación personalizada
        confirm = tk.Toplevel(self)
        confirm.title("Confirmar eliminación")
        confirm.geometry("430x120")
        confirm.resizable(False, False)
        tk.Label(confirm, text=f"¿Está seguro que desea eliminar\nel insumo '{nom}'?", font=('Helvetica', 12)).pack(pady=10)

        btn_frame = tk.Frame(confirm)
        btn_frame.pack(pady=10)

        def confirmar():
            result = self.controller.delIns(nom)
            if result == True:
                messagebox.showinfo('¡Eliminación exitosa!', 'Insumo eliminado de forma exitosa')
                self.nomInsList()
                self.nomInsCombo['values'] = self.nomInsListVal
                if self.nomInsListVal:
                    self.nomInsCombo.current(0)
                else:
                    self.nomInsCombo.set('')
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