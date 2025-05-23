class AppController:
    def __init__(self, app, model):
        self.app = app
        self.model = model

    def show_view(self, view_name):
        self.app.show_view(view_name)

    def show(self):
        result = self.model.show()
        return result