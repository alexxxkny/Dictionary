# Contain definition table/class which represents explaining of a term
# of particular class

import db_connection as db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Definition(db.Base):
    """Contain definition of a particular meaning of a term."""

    __tablename__ = 'definitions'

    id = Column(Integer, primary_key=True)
    definition = Column(String)
    term_id = Column(Integer, ForeignKey('terms.id'))

    term = relationship('Term', back_populates='definitions')

    def __init__(self, definition):
        self.definition = definition

    def __repr__(self):
        return f'Definition(id={self.id}, term_id={self.term_id},' \
               f' definition={self.definition})'
