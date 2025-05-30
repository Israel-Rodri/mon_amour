import tkinter as tk
from tkinter import messagebox
from views.base import BaseView

class BaseLoginView(tk.Frame):
    login = False
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.winfo_toplevel().config(menu=None)

        self.title = tk.Label(self, text=('Iniciar Sesión:'), font=('Helvetica', 14))
        self.title.grid(column=0, row=0)

        #Titulo y campo de entrada para correo
        self.userTitle = tk.Label(self, text='Correo electrónico:', font=('Helvetica', 14))
        self.userTitle.grid(column=0, row=1, pady=5, sticky='w')
        vcmdUser = (self.register(self.onValidate), '%P', '20')
        self.userEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdUser)
        self.userEntry.grid(column=1, row=1, pady=10, sticky='w')

        #Titulo y campo de entrada para contraseña
        self.passwordTitle = tk.Label(self, text='Contraseña:', font=('Helvetica', 14))
        self.passwordTitle.grid(column=0, row=2, pady=5, sticky='w')
        vcmdPassw = (self.register(self.onValidate), '%P', '15')
        self.passwordEntry = tk.Entry(self, font=('Helvetica', 14), validate='key', validatecommand=vcmdPassw, show='*')
        self.passwordEntry.grid(column=1, row=2, pady=10, sticky='w')

        self.loginBtn = tk.Button(self, text='Iniciar Sesión', font=('Helvetica', 14), command=lambda: self.login(self.userEntry.get(), self.passwordEntry.get()))
        self.loginBtn.grid(column=2, row=3, pady=10, sticky='w')

    def login(self, user, passw):
        if user == '' or passw == '':
            messagebox.showerror('Error', 'Debe rellenar todos los campos')
        else:
            result = self.controller.login(user, passw)
            if result == True:
                messagebox.showinfo('¡Inicio de sesión exitoso!', 'Ha iniciado sesión de forma exitosa')
                BaseLoginView.login = True
                self.userEntry.delete(0, tk.END)
                self.passwordEntry.delete(0, tk.END)
                self.controller.show_view('HomeView')

    #Funcion para limitar la cantidad de caracteres a escribir
    def onValidate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True