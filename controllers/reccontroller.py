#Clase del controlador
class RecController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

# -------- Mostrar -------- #

    #Comunicacion con la funcion show_view de app
    def show_view(self, view_name):
        self.app.show_view(view_name)

    def showRec(self):
        result = self.model.showRec()
        return result

    # -------- Agregar -------- #
    

    def insertRecNom(self, nom, desc):
        result = self.model.insertRecNom(nom, desc)
        return result

    def insertInsRec(self, rec, ins, can):
        result = self.model.insertInsRec(rec, ins, can)
        return result

    def nomProvList(self):
        result = self.model.nomProvList()
        return result

    def nomInsList(self):
        result = self.model.nomInsList()
        return result

    def nomRecList(self):
        result = self.model.nomRecList()
        return result

    # -------- Actualizar -------- #
    def updCanRec(self, rec, can):
        result = self.model.updCanRec(rec, can)
        return result