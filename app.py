from flask import Flask, render_template
import datetime
import requests
from dotenv import load_dotenv
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
        'api_key': os.getenv("API_KEY"),
        'regions': 'us',
        'markets': 'h2h',
        'oddsFormat': 'decimal',
        'dateFormat': 'iso',
        'bookmakers': 'draftkings'
    })

    games = []
    for game in odds_response.json():
        games.append(game['bookmakers'][0]['markets'][0]['outcomes'])

    return render_template('bets.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
