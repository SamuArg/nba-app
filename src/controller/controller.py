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

    def set_leaders(self):
        points_leaders = self.model.leaders[0]
        assists_leaders = self.model.leaders[1]
        rebounds_leaders = self.model.leaders[2]
        pts = []
        asts = []
        rbds = []
        for i in range(5):
            pts.append(f'{i+1}. {points_leaders[i].name} {round(points_leaders[i].points/points_leaders[i].games, 1)} PPG')
            asts.append(f'{i+1}. {assists_leaders[i].name} {round(assists_leaders[i].assists/assists_leaders[i].games, 1)} APG')
            rbds.append(f'{i+1}. {rebounds_leaders[i].name} {round(rebounds_leaders[i].rebounds/rebounds_leaders[i].games, 1)} RPG')
        self.view.set_leaders(pts, asts, rbds)