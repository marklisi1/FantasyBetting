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
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
    params={
        'api_key': os.getenv('API_KEY'),
        'regions': 'us',
        'markets': 'h2h,spreads',
        'oddsFormat': 'decimal',
        'dateFormat': 'iso',
    }
)
    return render_template('bets.html', odds_response=odds_response)

if __name__ == '__main__':
    app.run(debug=True)
