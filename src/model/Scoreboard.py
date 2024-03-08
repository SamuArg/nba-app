from nba_api.live.nba.endpoints import scoreboard
from .game import Game

class Scoreboard:
    @staticmethod
    def get_scoreboards():
        scoreboards = []
        games = scoreboard.ScoreBoard()
        scores = games.get_dict()['scoreboard']['games']
        for i in scores:
            game = Game(Scoreboard.get_score(i),Scoreboard.get_home_team(i),
                         Scoreboard.get_away_team(i),Scoreboard.get_period(i))
            scoreboards.append(game)
        return scoreboards
    
    def get_score(game):
        home_score = game['homeTeam']['score'] 
        away_score = game['awayTeam']['score']
        return (home_score, away_score)
    
    def get_home_team(game):
        return game['homeTeam']['teamTricode']
    
    def get_away_team(game):
        return game['awayTeam']['teamTricode']
    
    def get_period(game):
        return game['gameStatusText']