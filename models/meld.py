from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Boolean, ForeignKey
from db import Base, Player, MeldEntry

class Meld(Base):
    '''### junction table for player and meldentry that indicates player owns meld'''
    __tablename__ = 'meld'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    player_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    player:Mapped['Player'] = relationship('Player', back_populates='melds', uselist=False)
    cards:Mapped[List['MeldEntry']] = relationship('MeldEntry', back_populates='meld')
    rank:Mapped[int] = mapped_column(Integer)
    clean:Mapped[bool] = mapped_column(Boolean)
    