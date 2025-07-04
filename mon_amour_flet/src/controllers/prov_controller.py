from models.prov_model import ProvModel

class ProvController:
    def __init__(self):
        self.model = ProvModel()

    def show_prov(self):
        result = self.model.show_prov()
        return result
    
    def add_prov(self, rif, nom, tel, email):
        result = self.model.add_prov(rif, nom, tel, email)
        return result
    
    def trial(self, value):
        self.model.trial(value)