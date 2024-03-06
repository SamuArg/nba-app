class Game:
    def __init__(self, score, home_team, away_team, clock, period):
        self.score = score
        self.home_team = home_team
        self.away_team = away_team
        self.clock = clock
        self.period = period
    
    def print_game(self):
        print(f'Period : {self.period}, clock : {self.clock}, {self.home_team} {self.score[0]} - {self.score[1]} {self.away_team}')