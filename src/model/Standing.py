from nba_api.stats.endpoints import leaguestandingsv3
from model import Team
class Standing:
    @staticmethod
    def get_standing():
        teams = leaguestandingsv3.LeagueStandingsV3()
        teams = teams.get_dict()['resultSets'][0]['rowSet']
        standing = []
        for i in range(len(teams)):
            team = Team.Team(name=teams[i][4], city=teams[i][3], wins=teams[i][13],
                         loses=teams[i][14], win_percentage=teams[i][15],
                           rank=i+1, conference=teams[i][6], division=teams[i][10],
                           game_behind=teams[i][38])
            standing.append(team)
        return standing
    @staticmethod
    def get_conference_standing():
        league_standing = Standing.get_standing()
        conference_standing = ([],[])
        for i in league_standing:
            if i.conference == 'East':
                conference_standing[0].append(i)
            else:
                conference_standing[1].append(i)
        return conference_standing
conference = Standing.get_conference_standing()