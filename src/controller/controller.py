from model import Team
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def set_standing(self):
        east = self.view.east_standing
        for team in self.model.conference_standing[0]:
            row_position = east.rowCount()
            east.insertRow(row_position)
            name = QTableWidgetItem(team.name)
            name.setTextAlignment(Qt.AlignCenter)
            east.setItem(row_position, 0, name)
            wins = QTableWidgetItem(str(team.wins))
            wins.setTextAlignment(Qt.AlignCenter)
            east.setItem(row_position, 1, wins)
            loses = QTableWidgetItem(str(team.loses))
            loses.setTextAlignment(Qt.AlignCenter)
            east.setItem(row_position, 2, loses)
            win_percentage = QTableWidgetItem(str(team.win_percentage))
            win_percentage.setTextAlignment(Qt.AlignCenter)
            east.setItem(row_position, 3, win_percentage)
        east.reset()
        west = self.view.west_standing
        for team in self.model.conference_standing[1]:
            row_position = west.rowCount()
            west.insertRow(row_position)
            name = QTableWidgetItem(team.name)
            name.setTextAlignment(Qt.AlignCenter)
            west.setItem(row_position, 0, name)
            wins = QTableWidgetItem(str(team.wins))
            wins.setTextAlignment(Qt.AlignCenter)
            west.setItem(row_position, 1, wins)
            loses = QTableWidgetItem(str(team.loses))
            loses.setTextAlignment(Qt.AlignCenter)
            west.setItem(row_position, 2, loses)
            win_percentage = QTableWidgetItem(str(team.win_percentage))
            win_percentage.setTextAlignment(Qt.AlignCenter)
            west.setItem(row_position, 3, win_percentage)
