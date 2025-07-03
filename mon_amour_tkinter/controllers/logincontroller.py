#Clase del controlador
class LoginController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

    def login(self, user, passw):
        result = self.model.login(user, passw)
        return result

    #Comunicacion con la funcion show_view de app
    def show_view(self, view_name):
        self.app.show_view(view_name)