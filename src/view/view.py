from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

class Main_gui(QMainWindow):
    def __init__(self):
        super(Main_gui, self).__init__()
        uic.loadUi('src/view/main.ui', self)
        self.show()
    def clear_scoreboard(self):
        vbox = self.scores
        while vbox.count():
            item = vbox.takeAt(0)

            if isinstance(item, QSpacerItem):
                pass
            elif item.widget():
                item.widget().deleteLater()

    def set_scoreboard(self, games):
        for game in games:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(game.away_team))
            hbox.addWidget(QLabel(str(game.score[1])))
            hbox.addWidget(QLabel(str(game.period)))
            hbox.addWidget(QLabel(str(game.score[0])))
            hbox.addWidget(QLabel(game.home_team))
            self.scores.addLayout(hbox)

    def clear_standings(self):
        self.east_standing.clearContents()
        self.west_standing.clearContents()    

    def set_standings(self, standings):
        east = self.east_standing
        i = 0
        for team in standings[0]:
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
        west = self.west_standing
        west.clearContents()
        j = 0
        for team in standings[1]:
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