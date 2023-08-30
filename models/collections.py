from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from db import Base, Player, GameCardInstance, Game, Meld, Canasta
from typing import List

class DeckEntry(Base):
    '''### junction table for game and gamecardinstance that indicates card is in deck (not in play)'''
    __tablename__ = 'deckentry'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    cards:Mapped[List[GameCardInstance]] = relationship('GameCardInstance', back_populates='deck')
    game_ident:Mapped[int] = mapped_column(Integer, ForeignKey('game.ident'))
    game:Mapped['Game'] = relationship('Game', back_populates='deck', uselist=False)

class PileEntry(Base):
    '''### junction table for game and gamecardinstance that indicates card is in deck (not in play)'''
    __tablename__ = 'pileentry'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    cards:Mapped[List[GameCardInstance]] = relationship('GameCardInstance', back_populates='pile')
    game_ident:Mapped[int] = mapped_column(Integer, ForeignKey('game.ident'))
    game:Mapped['Game'] = relationship('Game', back_populates='pile', uselist=False)

class HandEntry(Base):
    '''### junction table for player and gamecardinstance that indicates card is in player's hand (not in play)'''
    __tablename__ = 'handentry'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    cards:Mapped[List[GameCardInstance]] = relationship('GameCardInstance', back_populates='hand')
    player_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    player:Mapped['Player'] = relationship('Player', back_populates='hand', uselist=False)

class FootEntry(Base):
    '''junction table for player and gamecardinstance that indicates card is in player's foot (not in play)'''
    __tablename__ = 'footentry'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    cards:Mapped[List[GameCardInstance]] = relationship('GameCardInstance', back_populates='foot')
    player_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    player:Mapped['Player'] = relationship('Player', back_populates='foot', uselist=False)

class MeldEntry(Base):
    '''junction table for meld and gamecardinstance that indicates card is in the meld (not in play)'''
    __tablename__ = 'meldentry'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    cards:Mapped[List[GameCardInstance]] = relationship('GameCardInstance', back_populates='meld')
    meld_ident:Mapped[int] = mapped_column(Integer, ForeignKey('meld.ident'))
    meld:Mapped['Meld'] = relationship('Meld', back_populates='cards', uselist=False)
    
class CanastaEntry(Base):
    '''junction table for canasta and gamecardinstance that indicates card is in the canasta (not in play)'''
    __tablename__ = 'canastaentry'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    cards:Mapped[List[GameCardInstance]] = relationship('GameCardInstance', back_populates='canasta')
    canasta_ident:Mapped[int] = mapped_column(Integer, ForeignKey('canasta.ident'))
    canasta:Mapped['Canasta'] = relationship('Canasta', back_populates='cards', uselist=False)
    