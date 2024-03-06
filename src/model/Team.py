class Team:
    def __init__(self, name, city, wins, loses, win_percentage, rank, conference, division, game_behind):
        self.name = name
        self.city = city
        self.wins = wins
        self.loses = loses
        self.win_percentage = win_percentage
        self.rank = rank
        self.conference = conference
        self.division = division
        self.game_behind = game_behind


    def __str__(self):
        return f"Team: {self.name}\n" \
               f"City: {self.city}\n" \
               f"Wins: {self.wins}\n" \
               f"Loses: {self.loses}\n" \
               f"Win Percentage: {self.win_percentage}\n" \
               f"Rank: {self.rank}\n" \
               f"Conference: {self.conference}\n" \
               f"Division: {self.division}\n" \
               f"Game Behind : {self.game_behind}"