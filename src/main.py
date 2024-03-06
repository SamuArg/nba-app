import controller.controller as controller
import view.view as view
import model.Model as model
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
class Main:
    def __init__(self, controller):
        self.controller = controller
        self.window = controller.view
        self.setup_timer()

    def setup_timer(self):
        self.timer = QTimer(self.window)
        self.timer.timeout.connect(self.update_every_30_seconds)
        self.timer.start(30000) 

    def update_every_30_seconds(self):
        self.controller.set_standing()
        self.controller.set_scoreboard()

if __name__ == '__main__':
    app = QApplication([])
    main = Main(controller.Controller(view.Main_gui(), model.Model()))
    main.controller.set_standing()
    main.controller.set_scoreboard()
    app.exec_()