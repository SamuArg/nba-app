import controller.controller as controller
import view.view as view
import model.Model as model
from PyQt5.QtWidgets import *
class Main:
    def __init__(self, controller):
        self.controller = controller
        self.window = controller.view

if __name__ == '__main__':
    app = QApplication([])
    main = Main(controller.Controller(view.Main_gui(), model.Model()))
    app.exec_()