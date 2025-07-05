from models.ins_model import InsModel

class InsController:
    def __init__(self):
        self.model = InsModel()

    def show_ins(self):
        result = self.model.show_ins()
        return result
    
    def add_ins(self, nom, desc, med, can, pre):
        result = self.model.add_ins (nom, desc, med, can, pre)
        return result
    
    def del_ins(self, values):
        result = self.model.del_ins(values)
        return result
    
    def edit_ins(self, id, nom, desc, med, can, pre):
        result = self.model.edit_ins(id, nom, desc, med, can, pre)
        return result