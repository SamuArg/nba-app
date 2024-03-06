from model import Team
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def set_standing(self):
        east = self.view.east_standing
        east.clearContents()
        i = 0
        for team in self.model.conference_standing[0]:
            name = QTableWidgetItem(team.name)
            name.setTextAlignment(Qt.AlignCenter)
            east.setItem(i, 0, name)
            wins = QTableWidgetItem(str(team.wins))
            wins.setTextAlignment(Qt.AlignCenter)
            east.setItem(i, 1, wins)
            loses = QTableWidgetItem(str(team.loses))
            loses.setTextAlignment(Qt.AlignCenter)
            east.setItem(i, 2, loses)
            win_percentage = QTableWidgetItem(str(team.win_percentage))
            win_percentage.setTextAlignment(Qt.AlignCenter)
            east.setItem(i, 3, win_percentage)
            i += 1
        west = self.view.west_standing
        west.clearContents()
        j = 0
        for team in self.model.conference_standing[1]:
            name = QTableWidgetItem(team.name)
            name.setTextAlignment(Qt.AlignCenter)
            west.setItem(j, 0, name)
            wins = QTableWidgetItem(str(team.wins))
            wins.setTextAlignment(Qt.AlignCenter)
            west.setItem(j, 1, wins)
            loses = QTableWidgetItem(str(team.loses))
            loses.setTextAlignment(Qt.AlignCenter)
            west.setItem(j, 2, loses)
            win_percentage = QTableWidgetItem(str(team.win_percentage))
            win_percentage.setTextAlignment(Qt.AlignCenter)
            west.setItem(j, 3, win_percentage)
            j += 1
    
    def set_scoreboard(self):
        vbox = self.view.scores
        for game in self.model.scoreboard:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(game.away_team))
            hbox.addWidget(QLabel(str(game.score[1])))
            hbox.addWidget(QLabel(str(game.period)))
            hbox.addWidget(QLabel(str(game.score[0])))
            hbox.addWidget(QLabel(game.home_team))
            vbox.addLayout(hbox)

