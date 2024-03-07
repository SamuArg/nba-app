from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont
import os
class Main_gui(QMainWindow):
    def __init__(self):
        super(Main_gui, self).__init__()
        ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.ui'))
        uic.loadUi(ui_path, self)
        self.setWindowTitle('NBA app')
        self.show()

    def clear_scoreboard(self):
        scores_widget = self.scores

        while scores_widget.count():
            item = scores_widget.takeAt(0)

            if item.widget():
                widget = item.widget()
                widget.setParent(None)
                widget.deleteLater()

            elif item.layout():
                sub_layout = item.layout()
                self.clear_layout(sub_layout)

        scores_widget.update()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            if item.widget():
                widget = item.widget()
                widget.setParent(None)
                widget.deleteLater()

            elif item.layout():
                sub_layout = item.layout()
                self.clear_layout(sub_layout)

    def set_scoreboard(self, games):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        for game in games:
            #Create Hbox for each game
            hbox = QHBoxLayout()

            #Create Vbox for team logo and name
            away_layout = QVBoxLayout()

            #Away team logo
            away_logo = QLabel()
            away_logo_path = os.path.join(script_directory, 'images', game.away_team + '.png')
            pixmap = QPixmap(away_logo_path).scaledToHeight(60, Qt.SmoothTransformation)
            away_logo.setPixmap(pixmap)
            away_logo.setAlignment(Qt.AlignHCenter)
            away_layout.addWidget(away_logo)

            #Away team label
            away_team_label = QLabel(game.away_team)
            away_team_label.setAlignment(Qt.AlignHCenter)
            away_layout.addWidget(away_team_label)
            hbox.addLayout(away_layout)

            #Score and game status
            score_label = QLabel(str(game.score[1]))
            score_label.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
            score_label.setFont(QFont('Open Sans', 16))
            hbox.addWidget(score_label)

            period_label = QLabel(str(game.period))
            period_label.setAlignment(Qt.AlignCenter)
            hbox.addWidget(period_label)

            score_label_2 = QLabel(str(game.score[0]))
            score_label_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
            score_label_2.setFont(QFont('Open Sans',16))
            hbox.addWidget(score_label_2)

            #Home team Vbox
            home_layout = QVBoxLayout()

            #Home team logo
            home_logo = QLabel()
            home_logo_path = os.path.join(script_directory, 'images', game.home_team + '.png')
            pixmap = QPixmap(home_logo_path).scaledToWidth(60, Qt.SmoothTransformation)
            home_logo.setPixmap(pixmap)
            home_logo.setAlignment(Qt.AlignHCenter)
            home_layout.addWidget(home_logo)

            #Home team label
            home_team_label = QLabel(game.home_team)
            home_team_label.setAlignment(Qt.AlignHCenter)
            home_layout.addWidget(home_team_label)

            hbox.addLayout(home_layout)
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
        east.setEditTriggers(QTableWidget.NoEditTriggers)
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
        west.setEditTriggers(QTableWidget.NoEditTriggers)
        east.resizeColumnsToContents()
        east.resizeRowsToContents()

        west.resizeColumnsToContents()
        west.resizeRowsToContents()
        east.resize(east.horizontalHeader().length() + east.verticalHeader().width() + 5,
        east.verticalHeader().length() + east.horizontalHeader().height() + 5)

        west.resize(west.horizontalHeader().length() + west.verticalHeader().width() + 5,
        west.verticalHeader().length() + west.horizontalHeader().height()  + 5)
