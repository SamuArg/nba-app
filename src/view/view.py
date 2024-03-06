from PyQt5.QtWidgets import *
from PyQt5 import uic

class Main_gui(QMainWindow):
    def __init__(self):
        super(Main_gui, self).__init__()
        uic.loadUi('src/view/main.ui', self)
        self.show()