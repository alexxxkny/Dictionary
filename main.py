# Starting point of the app.

import db_api
import db_connection as db
from term import Term
from sentence import Sentence
from definition import Definition
from set import Set
from term_class import TermClass
from sqlalchemy import select
from sqlalchemy.orm import Session
from cli import app


if __name__ == '__main__':
    db.mapper_registry.metadata.create_all(db.engine)
    with Session(db.engine) as session:
        # db_api.full_default_db(session)
        app(obj={'session': session})

