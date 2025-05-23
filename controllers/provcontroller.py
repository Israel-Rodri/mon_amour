from models.provmodels import Model

class Controller():
    def __init__(self, model):
        self.model = model

    def insertar(self, rif, nom, tel, email):
        result = self.model.insert(rif, nom, tel, email)
        return result

    def show(self):
        result = self.model.show()
        return result