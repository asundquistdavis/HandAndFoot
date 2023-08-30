from models.player import Player
from models.meld import Meld
from models.canasta import Canasta
from models.game import Game
from models.gamecardinstance import GameCardInstance
from models.card import Card
from models.collections import DeckEntry, PileEntry, HandEntry, FootEntry, MeldEntry, CanastaEntry
from db import DB, Base
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    bundle = '\\static\\index.js'
    return render_template('index.html', bundle=bundle)

if __name__ == '__main__':
    Base.metadata.create_all(DB.engine())
    app.run(debug=True)
