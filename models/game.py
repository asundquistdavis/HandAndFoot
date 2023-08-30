from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from db import Base, Player, GameCardInstance, DeckEntry, PileEntry
from typing import List

class Game(Base):
    '''### individual game'''
    __tablename__ = 'game'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    host_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    game_player_infos:Mapped[List['Player']] = relationship('Player', back_populates='game')
    # game state variables
    hand_number:Mapped[int] = mapped_column(Integer, default=0)
    dealer_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    turn_number:Mapped[int] = mapped_column(Integer, default=0)
    active_player_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    # collections
    cards:Mapped[List['GameCardInstance']] = relationship('GameCardInstance', back_populates='game')
    deck:Mapped[List['DeckEntry']] = relationship('DeckEntry', back_populates='game')
    pile:Mapped[List['PileEntry']] = relationship('PileEntry', back_populates='game')
