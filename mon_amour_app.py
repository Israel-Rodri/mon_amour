import tkinter as tk
from views.home import HomeView
from views.prov.showProv import ShowProvView
from views.prov.addProv import AddProvView
from views.insumos.showIns import ShowInsView
from controllers.appcontroller import AppController
from models.appmodels import Model

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación Tkinter")
        self.geometry("1100x700")
        self.resizable(width=False, height=False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.model = Model()
        self.appcontroller = AppController(self, self.model)

        self.views = {}  # Diccionario de vistas
        for F in (HomeView, ShowProvView, ShowInsView, AddProvView):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self.appcontroller)
            self.views[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  

        self.show_view("HomeView")

    def show_view(self, view_name):
        frame = self.views[view_name]
        frame.tkraise()  # Trae la vista al frente
        self.update_idletasks()

if __name__ == "__main__":
    app = App()
    app.mainloop()