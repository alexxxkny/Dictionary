# This file contains Term table/class

import db_connection as db
from sqlalchemy import Column, String, Integer


class Term(db.Base):
    __tablename__ = 'term'

    id = Column(Integer, primary_key=True)
    term = Column(String)
    translation = Column(String)

    def __repr__(self):
        return f'#{self.id} {self.term} - {self.translation}'
