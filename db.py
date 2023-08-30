from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import DeclarativeBase, Session
from typing import TypeVar, List
import os
from config import REMOTE

T = TypeVar('T')

class Base(DeclarativeBase):
    
    def __json__(self, parent:str=None)->dict:
        ...

def json(instance:Base, parent:str=None, packable:str=False)->dict:
    '''
    ### returns a json serializable representation of object.
    calls __json__(self, ...) on the object
    '''
    if instance: return instance.__json__(parent)
    return {} if packable else None

class DB(Session):
    
    REMOTE = os.environ.get('REMOTE', None) or REMOTE

    _remote_db_url = f''
    _local_db_url = 'sqlite:///db.db'

    db_url = _remote_db_url if REMOTE else _local_db_url

    def engine()->Engine:
        return create_engine(DB.db_url)

    def match(self, Table:T, **conditions)->T:
        self.query(Table).filter_by(**conditions)

    def __init__(self):
        super().__init__(bind=DB.db_url)

class Player:
    '''### individual player'''
    ident:int
    name:str
    game_ident:int
    game:'Game'
    # player state variables
    score:int
    # collections
    hand:List['HandEntry']
    foot:List['HandEntry']
    melds:List['Meld']
    canastas:List['Canasta']

class Meld:
    '''### junction table for player and meldentry that indicates player owns meld'''
    ident:int
    player_ident:int
    player:'Player'
    cards:List['MeldEntry']
    rank:int
    clean:bool

class Canasta:
    '''### junction table for player and canastaentry that indicates player owns canasta'''
    ident:int
    player_ident:int
    player:'Player'
    cards:List['CanastaEntry']
    rank:int
    clean:bool

class Game:
    '''### individual game'''
    ident:int
    host_ident:int
    game_player_infos:List['Player']
    # game state variables
    hand_number:int
    dealer_ident:int
    turn_number:int
    active_player_ident:int
    # collections
    cards:List['GameCardInstance']
    deck:List['DeckEntry']
    pile:List['PileEntry']

class GameCardInstance:
    '''### junction table for card and game that indicates card is part of game'''
    ident:int
    game_ident:int
    game:'Game'
    card_ident:int
    card:'Card'
    instance_number:int
    # reverse collection
    deck_indent:int
    deck:'DeckEntry'
    pile_indent:int
    pile:'PileEntry'
    hand_indent:int
    hand:'HandEntry'
    foot_indent:int
    foot:'FootEntry'
    meld_indent:int
    meld:'MeldEntry'
    canasta_indent:int
    canasta:'CanastaEntry'

class Card:
    ident:int
    game_card_instances:List['GameCardInstance']
    suit:int # 0: wild, 1: hearts, 2: spades, 3: diamonds, 4: clubs
    rank:int # 0-13

class DeckEntry:
    '''### junction table for game and gamecardinstance that indicates card is in deck (not in play)'''
    ident:int
    cards:List[GameCardInstance]
    game_ident:int
    game:'Game'

class PileEntry:
    '''### junction table for game and gamecardinstance that indicates card is in deck (not in play)'''
    ident:int
    cards:List[GameCardInstance]
    game_ident:int
    game:'Game'

class HandEntry:
    '''### junction table for player and gamecardinstance that indicates card is in player's hand (not in play)'''
    ident:int
    cards:List[GameCardInstance]
    player_ident:int
    player:'Player'

class FootEntry:
    '''junction table for player and gamecardinstance that indicates card is in player's foot (not in play)'''
    ident:int
    cards:List[GameCardInstance]
    player_ident:int
    player:'Player'

class MeldEntry:
    '''junction table for meld and gamecardinstance that indicates card is in the meld (not in play)'''
    ident:int
    cards:List[GameCardInstance]
    meld_ident:int
    meld:'Meld'
    
class CanastaEntry:
    '''junction table for canasta and gamecardinstance that indicates card is in the canasta (not in play)'''
    ident:int
    cards:List[GameCardInstance]
    canasta_ident:int
    canasta:'Canasta'