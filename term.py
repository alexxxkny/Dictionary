# This file contains Term table/class. The main class of the app.

import db_connection as db
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Term(db.Base):
    """Contain term with its translation and other characteristics."""

    __tablename__ = 'terms'

    id = Column(Integer, primary_key=True)
    term = Column(String)
    translation = Column(String)
    class_id = Column(Integer, ForeignKey('term_classes.id'))
    set_id = Column(Integer, ForeignKey('sets.id'))
    last_revision = Column(DateTime, default=datetime.now())
    # success_rate

    set = relationship('Set', back_populates='terms')
    term_class = relationship('TermClass', back_populates='terms')
    sentences = relationship('Sentence', back_populates='term')
    definitions = relationship('Definition', back_populates='term')

    def __init__(self, term, translation, term_class=None):
        self.term = term.strip().lower()
        self.translation = translation.strip().lower()
        self.term_class = term_class

    def __repr__(self):
        return f'Term(id={self.id}, term={self.term}, translation={self.translation})'
