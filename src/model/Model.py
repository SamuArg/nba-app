from model import Standing
from model import Scoreboard
class Model:
    def __init__(self):
        self.scoreboard = Scoreboard.Scoreboard.get_scoreboards()
        self.standing = Standing.Standing.get_standing()
        self.conference_standing = Standing.Standing.get_conference_standing()

    def update(self):
        self.scoreboard = Scoreboard.Scoreboard.get_scoreboards()
        self.standing = Standing.Standing.get_standing()
        self.conference_standing = Standing.Standing.get_conference_standing()