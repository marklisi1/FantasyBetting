from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from app.models import User
from app.forms import RegistrationForm, LoginForm
import requests
import os

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        print('yeeeeup')
        return redirect('/')

    return render_template('register.html', form=form)
