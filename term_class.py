import db_connection as db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class TermClass(db.Base):
    __tablename__ = 'term_classes'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    terms = relationship('Term', back_populates='term_class')
    definitions = relationship('Definition', back_populates='term_class')

    def __repr__(self):
        return f'#{self.id} {self.name}'
