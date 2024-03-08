from PyQt5.QtWidgets import *
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def set_standing(self):
        self.view.clear_standings()
        self.view.set_standings(self.model.conference_standing)
    
    def set_scoreboard(self):
        self.model.update()
        games = self.model.scoreboard
        self.view.clear_scoreboard()
        self.view.set_scoreboard(games)
    def set_size(self):
        self.view.set_size()