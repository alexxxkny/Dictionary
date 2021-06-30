# This file contains table/class sentence

import db_connection as db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class Sentence(db.Base):
    """Contain example of using particular term."""

    __tablename__ = 'sentences'

    id = Column(Integer, primary_key=True)
    term_id = Column(Integer, ForeignKey('terms.id'))
    sentence = Column(String)

    term = relationship('Term', back_populates='sentences')

    def __repr__(self):
        return f'Sentence(id={self.id}, term_id={self.term_id}, sentence={self.sentence})'
