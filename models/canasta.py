from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Boolean, ForeignKey
from db import Base, Player, CanastaEntry

class Canasta(Base):
    '''### junction table for player and canastaentry that indicates player owns canasta'''
    __tablename__ = 'canasta'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    player_ident:Mapped[int] = mapped_column(Integer, ForeignKey('player.ident'))
    player:Mapped['Player'] = relationship('Player', back_populates='canastas', uselist=False)
    cards:Mapped[List['CanastaEntry']] = relationship('CanastaEntry', back_populates='canasta')
    rank:Mapped[int] = mapped_column(Integer)
    clean:Mapped[bool] = mapped_column(Boolean)
    