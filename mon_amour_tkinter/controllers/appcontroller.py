#Clase del controlador
class AppController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

# -------- Mostrar -------- #

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
        result = self.model.showInsRec()
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

    #Comunicacion con la funcion insertProv de models
    def insertProv(self, rif, nom, tel, email):
        result = self.model.insertProv(rif, nom, tel, email)
        return result

    def insertIns(self, nom, desc, med, can, rif, pre):
        result = self.model.insertIns(nom, desc, med, can, rif, pre)
        return result

    def insertRecNom(self, nom, desc):
        result = self.model.insertRecNom(nom, desc)
        return result

    def insertInsRec(self, rec, ins, can):
        result = self.model.insertInsRec(rec, ins, can)
        return result

# -------- Actualizar -------- #
    def updCanRec(self, rec, can):
        result = self.model.updCanRec(rec, can)
        return result

    def updIns(self, ins, nom, desc, med, can, pre):
        result = self.model.updIns(ins, nom, desc, med, can, pre)
        return result

    def updProv(self, nomAct, nom, tel, email):
        from controllers.provcontroller import ProvController
        prov = ProvController(self.app, self.model)
        result = prov.upProv(nomAct, nom, tel, email)
        return result

# -------- Eliminar -------- #
    def delProv(self, nom):
        result = self.model.delProv(nom)
        return result
    
    def delIns(self, ins):
        result = self.model.delIns(ins)
        return result
    
    def delRec(self, rec):
        result = self.model.delRec(rec)
        return result

# -------- Login -------- #
    def login(self, user, passw):
        result = self.model.login(user, passw)
        return result