from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from db import Base, GameCardInstance
from typing import List

class Card(Base):
    __tablename__ = 'card'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    game_card_instances:Mapped[List['GameCardInstance']] = relationship('GameCardInstance', back_populates='card')
    suit:Mapped[int] = mapped_column(Integer) # 0: wild, 1: hearts, 2: spades, 3: diamonds, 4: clubs
    rank:Mapped[int] = mapped_column(Integer) # 0-13
