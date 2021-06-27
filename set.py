import db_connection as db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Set(db.Base):
    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    terms = relationship('Term', back_populates='set')

    def __repr__(self):
        return f'Set(id={self.id}, name={self.name})'
