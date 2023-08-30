from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from db import Base, Meld, Canasta, Game, HandEntry, FootEntry

class Player(Base):
    '''### individual player'''
    __tablename__ = 'player'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String)
    game_ident:Mapped[int] = mapped_column(Integer, ForeignKey('game.ident'))
    game:Mapped['Game'] = relationship('Game', back_populates='players', uselist=False)
    # player state variables
    score:Mapped[int] = mapped_column(Integer, default=0)
    # collections
    hand:Mapped[List['HandEntry']] = relationship('HandEntry', back_populates='player')
    foot:Mapped[List['FootEntry']] = relationship('FootEntry', back_populates='player')
    melds:Mapped[List['Meld']] = relationship('Meld', back_populates='player')
    canastas:Mapped[List['Canasta']] = relationship('Canasta', back_populates='player')
    