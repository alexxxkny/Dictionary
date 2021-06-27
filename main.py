import db_connection as db
from term import Term
from sentence import Sentence
from sqlalchemy import select
from sqlalchemy.orm import Session


if __name__ == '__main__':
    db.mapper_registry.metadata.create_all(db.engine)
    with Session(db.engine) as session:
        term1 = Term(term='bedside table', translation='тумбочка')
        term2 = Term(term='cooker', translation='плита')
        session.add_all((term1, term2))
        session.commit()
        term1.sentences = [Sentence(sentence='There is a phone on my bedside table'),
                           Sentence(sentence='I forgot keys in the bedside table')]
        terms = session.execute(select(Term)).all()
        for term in terms:
            print(term)