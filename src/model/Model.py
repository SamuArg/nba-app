from model import Standing
from model import Scoreboard
from model import Stats
class Model:
    def __init__(self):
        self.scoreboard = Scoreboard.Scoreboard.get_scoreboards()
        self.standing = Standing.Standing.get_standing()
        self.conference_standing = Standing.Standing.get_conference_standing()
        self.stats = Stats.Stats()
        self.leaders = (self.stats.get_scoring_leaders(), self.stats.get_assists_leaders(), self.stats.get_rebounds_leaders())
        

    def update(self):
        self.scoreboard = Scoreboard.Scoreboard.get_scoreboards()
        self.standing = Standing.Standing.get_standing()
        self.conference_standing = Standing.Standing.get_conference_standing()
        self.leaders = (self.stats.get_scoring_leaders(), self.stats.get_assists_leaders(), self.stats.get_rebounds_leaders())