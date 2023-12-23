from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard


app = Flask(__name__)


@app.route("/")
def home():
    games = scoreboard.ScoreBoard().games.get_dict()
    game_count = get_game_count(games)
    matchups = get_matchups(games)
    return render_template("index.html", game_count=game_count, matchups=matchups)

def get_game_count(games):
    for index, game in enumerate(games):
        pass
    game_count = index + 1
    return game_count

def get_matchups(games):
    matchups = []
    for game in games:
        home_team = game["homeTeam"]["teamCity"] + " " + game["homeTeam"]["teamName"]
        away_team = game["awayTeam"]["teamCity"] + " " + game["awayTeam"]["teamName"]
        matchups.append(home_team + " vs " + away_team)
    
    return matchups

if __name__ == "__main__":
    app.run(debug=True)