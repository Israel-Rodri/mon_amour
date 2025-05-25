#Clase del controlador
class AppController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

    #Comunicacion con la funcion show_view de app
    def show_view(self, view_name):
        self.app.show_view(view_name)

    #Comunicacion con la funcion showProv de models
    def showProv(self):
        result = self.model.showProv()
        return result

    #Comunicacion con la funcion showIns de models
    def showIns(self):
        result = self.model.showIns()
        return result

    def showRec(self):
        result = self.model.showRec()
        return result

    def showInsRec(self):
        result = self.model.showRec()
        return result

    def nomProvList(self):
        result = self.model.nomProvList()
        return result

    #Comunicacion con la funcion insertProv de models
    def insertProv(self, rif, nom, tel, email):
        result = self.model.insertProv(rif, nom, tel, email)
        return result

    def insertIns(self, nom, desc, med, can, rif, pre):
        result = self.model.insertIns(nom, desc, med, can, rif, pre)
        return result