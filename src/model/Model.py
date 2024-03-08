from .standing import Standing
from .scoreboard import Scoreboard
from .stats import Stats
class Model:
    def __init__(self):
        self.scoreboard = Scoreboard.get_scoreboards()
        self.standing = Standing.get_standing()
        self.conference_standing = Standing.get_conference_standing()
        self.stats = Stats()
        self.leaders = (self.stats.get_scoring_leaders(), self.stats.get_assists_leaders(), self.stats.get_rebounds_leaders())
        

    def update(self):
        self.scoreboard = Scoreboard.get_scoreboards()
        self.standing = Standing.get_standing()
        self.conference_standing = Standing.get_conference_standing()
        self.leaders = (self.stats.get_scoring_leaders(), self.stats.get_assists_leaders(), self.stats.get_rebounds_leaders())