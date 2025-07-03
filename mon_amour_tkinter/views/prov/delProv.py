import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.prov.baseprov import BaseProvView

class DelProvView(BaseProvView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        # Título de la sección
        self.title = tk.Label(self, text='Eliminar Proveedor', font=('Helvetica', 18, 'bold'))
        self.title.grid(column=1, row=0, pady=10, sticky='w')

        # Lista desplegable de proveedores
        self.nomProvTitle = tk.Label(self, text='Nombre Proveedor:', font=('Helvetica', 14))
        self.nomProvTitle.grid(column=2, row=1, pady=5, sticky='w')
        self.nomProvCombo = ttk.Combobox(self, font=('Helvetica', 14), state='readonly')
        self.nomProvListVal = []
        self.nomProvList()
        self.nomProvCombo['values'] = self.nomProvListVal
        if self.nomProvListVal:
            self.nomProvCombo.current(0)
        self.nomProvCombo.grid(column=3, row=1, pady=5, padx=5, sticky='w')

        # Botón para eliminar proveedor
        self.delProvBtn = tk.Button(
            self,
            text='Eliminar proveedor',
            font=('Helvetica', 14),
            command=self.delProv
        )
        self.delProvBtn.grid(column=2, row=2, pady=10, sticky='w')

    def nomProvList(self):
        nomList = self.controller.nomProvList()
        self.nomProvListVal.clear()
        for i in nomList:
            self.nomProvListVal.append(i[0])

    def delProv(self):
        nom = self.nomProvCombo.get()
        if not nom:
            messagebox.showerror('Error', 'Seleccione un proveedor para eliminar')
            return

        # Ventana de confirmación personalizada
        confirm = tk.Toplevel(self)
        confirm.title("Confirmar eliminación")
        confirm.geometry("430x120")
        confirm.resizable(False, False)
        tk.Label(confirm, text=f"¿Está seguro que desea eliminar\nal proveedor '{nom}'?", font=('Helvetica', 12)).pack(pady=10)

        btn_frame = tk.Frame(confirm)
        btn_frame.pack(pady=10)

        def confirmar():
            result = self.controller.delProv(nom)
            if result == True:
                messagebox.showinfo('¡Eliminación exitosa!', 'Proveedor eliminado de forma exitosa')
                self.nomProvList()
                self.nomProvCombo['values'] = self.nomProvListVal
                if self.nomProvListVal:
                    self.nomProvCombo.current(0)
                else:
                    self.nomProvCombo.set('')
            else:
                messagebox.showerror('Error', result)
            confirm.destroy()

        def cancelar():
            confirm.destroy()

        tk.Button(btn_frame, text="Sí", font=('Helvetica', 12), width=8, command=confirmar).pack(side='left', padx=10)
        tk.Button(btn_frame, text="No", font=('Helvetica', 12), width=8, command=cancelar).pack(side='right', padx=10)