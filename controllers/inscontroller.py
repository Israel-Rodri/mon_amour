#Clase del controlador
class InsController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

# -------- Mostrar -------- #

    #Comunicacion con la funcion show_view de app
    def show_view(self, view_name):
        self.app.show_view(view_name)

    #Comunicacion con la funcion showIns de models
    def showIns(self):
        result = self.model.showIns()
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

    # -------- Agregar -------- #
    def insertIns(self, nom, desc, med, can, rif, pre):
        result = self.model.insertIns(nom, desc, med, can, rif, pre)
        return result

    # -------- Actualizar -------- #
    def updIns(self, ins, nom, desc, med, can, pre):
        result = self.model.updIns(ins, nom, desc, med, can, pre)
        return result