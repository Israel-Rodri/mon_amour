class AppController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

    def show_view(self, view_name):
        self.app.show_view(view_name)

    def showProv(self):
        result = self.model.showProv()
        return result

    def showIns(self):
        result = self.model.showIns()
        return result