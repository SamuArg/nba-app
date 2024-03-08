from controller.controller import Controller
from view.view import Main_gui
from model.model import Model
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
class Main:
    def __init__(self, controller):
        self.controller = controller
        self.window = controller.view
        self.setup_timer()

    def setup_timer(self):
        self.timer = QTimer(self.window)
        self.timer2 = QTimer(self.window)
        self.timer.timeout.connect(self.controller.set_scoreboard)
        self.timer.start(30000)
        self.timer2.timeout.connect(self.controller.set_standing)
        self.timer2.start(900000)

if __name__ == '__main__':
    app = QApplication([])
    main = Main(Controller(Main_gui(), Model()))
    main.controller.set_standing()
    main.controller.set_scoreboard()
    main.controller.set_size()
    main.controller.set_leaders()
    app.exec_()