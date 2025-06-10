#Clase del controlador
class ProvController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

#Comunicacion con la funcion showProv de models
    def showProv(self):
        result = self.model.showProv()
        return result
    
    #Comunicacion con la funcion insertProv de models
    def insertProv(self, rif, nom, tel, email):
        result = self.model.insertProv(rif, nom, tel, email)
        return result

    def show_view(self, view_name):
        self.app.show_view(view_name)

    def nomProvList(self):
        result = self.model.nomProvList()
        return result

    def nomInsList(self):
        result = self.model.nomInsList()
        return result

    def nomRecList(self):
        result = self.model.nomRecList()
        return result