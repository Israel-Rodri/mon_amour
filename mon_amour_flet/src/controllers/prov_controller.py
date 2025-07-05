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
    
    def del_prov(self, values):
        result = self.model.del_prov(values)
        return result
    
    def edit_prov(self, rif, nom, tel, email):
        result = self.model.edit_prov(rif, nom, tel, email)
        return result