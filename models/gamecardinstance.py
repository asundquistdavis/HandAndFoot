from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from db import Base, Game, HandEntry, FootEntry, Card, DeckEntry, PileEntry,MeldEntry, CanastaEntry

class GameCardInstance(Base):
    '''### junction table for card and game that indicates card is part of game'''
    __tablename__ = 'gamecardinstance'
    ident:Mapped[int] = mapped_column(Integer, primary_key=True)
    game_ident:Mapped[int] = mapped_column(Integer, ForeignKey('game.ident'))
    game:Mapped['Game'] = relationship('game', back_populates='cards', uselist=False)
    card_ident:Mapped[int] = mapped_column(Integer, ForeignKey('card.ident'))
    card:Mapped['Card'] = relationship('Card', back_populates='gamecardinstances', uselist=False)
    instance_number:Mapped[int] = mapped_column(Integer)
    # reverse collection
    deck_indent:Mapped[int] = mapped_column(Integer, ForeignKey('deckentry.ident'))
    deck:Mapped['DeckEntry'] = relationship('DeckEntry', back_populates='cards', uselist=False)
    pile_indent:Mapped[int] = mapped_column(Integer, ForeignKey('pileentry.ident'))
    pile:Mapped['PileEntry'] = relationship('PileEntry', back_populates='cards', uselist=False)
    hand_indent:Mapped[int] = mapped_column(Integer, ForeignKey('handentry.ident'))
    hand:Mapped['HandEntry'] = relationship('HandEntry', back_populates='cards', uselist=False)
    foot_indent:Mapped[int] = mapped_column(Integer, ForeignKey('footentry.ident'))
    foot:Mapped['FootEntry'] = relationship('FoorEntry', back_populates='cards', uselist=False)
    meld_indent:Mapped[int] = mapped_column(Integer, ForeignKey('meldentry.ident'))
    meld:Mapped['MeldEntry'] = relationship('MeldEntry', back_populates='cards', uselist=False)
    canasta_indent:Mapped[int] = mapped_column(Integer, ForeignKey('canastaentry.ident'))
    canasta:Mapped['CanastaEntry'] = relationship('CanastaEntry', back_populates='cards', uselist=False)
