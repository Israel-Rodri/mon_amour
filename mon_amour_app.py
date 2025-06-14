#Importacion de todo lo necesario, no se si se puede hacer mejor
import tkinter as tk
from views.home import HomeView
from views.prov.showProv import ShowProvView
from views.prov.addProv import AddProvView
from views.prov.updProv import UpdProvView
from views.insumos.showIns import ShowInsView
from views.insumos.addIns import AddInsView
from views.insumos.updIns import UpdInsView
from views.recetas.showRec import ShowRecView
from views.recetas.addRec import AddRecView
from views.recetas.updRec import UpdRecView
from views.login.baselogin import BaseLoginView
from views.insumos_recetas.showInsRec import ShowInsRecView
from controllers.appcontroller import AppController
from models.appmodels import Model

#Clase principal de la aplicacion
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación Tkinter")
        self.geometry("1500x700")
        self.state('zoomed')
        self.resizable(width=False, height=False)

        #Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.model = Model()
        self.appcontroller = AppController(self, self.model)

        #Diccionario que agrupa las views disponibles
        self.views = {} 
        for F in (HomeView, ShowProvView, ShowInsView, AddProvView, ShowRecView, ShowInsRecView, AddInsView, AddRecView, UpdRecView, UpdInsView, BaseLoginView, UpdProvView):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self.appcontroller)
            self.views[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  

        #self.show_view("BaseLoginView")
        self.show_view("HomeView")

    #Funcion que permite visualizar las views
    def show_view(self, view_name):
        frame = self.views[view_name]
        if hasattr(frame, 'onShow'):
            frame.onShow()
        #Trae la vista al frente
        frame.tkraise()  
        self.update_idletasks()

#Bucle principal para la ejecucion de la aplicacion
if __name__ == "__main__":
    app = App()
    app.mainloop()