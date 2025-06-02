import tkinter as tk
from views.login.baselogin import BaseLoginView

#Clase base para todas las views
class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)

        self.homebtn = tk.Button(self, text='Inicio', font=('Helvetica', 14), bg='darkblue', fg='white', command=lambda:self.controller.show_view('HomeView'))
        self.homebtn.place(x=10, y=10)

        self.provbtn = tk.Button(self, text='Proveedores', font=('Helvetica', 14), bg='darkblue', fg='white', command=lambda:self.controller.show_view('ShowProvView'))
        self.provbtn.place(x=10, y=60)

        self.insbtn = tk.Button(self, text='Insumos', font=('Helvetica', 14), bg='darkblue', fg='white', command=lambda:self.controller.show_view('ShowInsView'))
        self.insbtn.place(x=10, y=110)

        self.recbtn = tk.Button(self, text='Recetas', font=('Helvetica', 14), bg='darkblue', fg='white', command=lambda:self.controller.show_view('ShowRecView'))
        self.recbtn.place(x=10, y=160)

        self.insrecbtn = tk.Button(self, text='Insumos-Recetas', font=('Helvetica', 14), bg='darkblue', fg='white', command=lambda:self.controller.show_view('ShowInsRecView'))
        self.insrecbtn.place(x=10, y=210)