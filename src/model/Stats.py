from .player import Player
from nba_api.stats.endpoints import leagueleaders

class Stats:
    def __init__(self):
        self.players_list = leagueleaders.LeagueLeaders().get_dict()['resultSet']['rowSet']
        self.players = self.get_players()

    def get_players(self):
        players = []
        for player in self.players_list:
            new_player = Player(name=player[2], points=player[24], assists=player[19], rebounds=player[18], games=player[5])
            players.append(new_player)
        return players
    
    def get_scoring_leaders(self, amount=5):
        return sorted(self.players, key=lambda x : x.points/x.games, reverse=True)[:amount]
    
    def get_assists_leaders(self, amount=5):
        return sorted(self.players, key=lambda x : x.assists/x.games, reverse=True)[:amount]
    
    def get_rebounds_leaders(self,amount=5):
        return sorted(self.players, key=lambda x : x.rebounds/x.games, reverse=True)[:amount]
