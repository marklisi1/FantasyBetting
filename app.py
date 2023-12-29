from flask import Flask, render_template
import datetime
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bets')
def bets():
    odds_response = requests.get(
    'https://api.the-odds-api.com/v4/sports/basketball_nba/odds',
    params={
        'api_key': '9bbb3bda82ce604880f9160ed6b6497c',
        'regions': 'us',
        'markets': 'h2h',
        'oddsFormat': 'decimal',
        'dateFormat': 'iso',
        'bookmakers': 'draftkings'
    })

    games = []
    for game in odds_response.json():
        home_team = game['bookmakers'][0]['markets'][0]['outcomes'][0]['name']
        home_odds = game['bookmakers'][0]['markets'][0]['outcomes'][0]['price']
        away_team = game['bookmakers'][0]['markets'][0]['outcomes'][1]['name']
        away_odds = game['bookmakers'][0]['markets'][0]['outcomes'][1]['price']
        games.append(f'{home_team} ({home_odds}) versus {away_team} ({away_odds})')


    return render_template('bets.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
