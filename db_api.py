# DB API

from sqlalchemy import select
from term import Term
from term_class import TermClass
from set import Set
from sentence import Sentence
from definition import Definition


def full_default_db(session):
    classes = [TermClass(name='verb'),
               TermClass(name='noun'),
               TermClass(name='adjective'),
               TermClass(name='adverb')]
    sets = [Set(name='general'),
            Set(name='inbox')]
    session.add_all(classes)
    session.add_all(sets)
    session.commit()


def get_table(session, table_name):
    table_to_class = {
        'terms': Term,
        'sets': Set,
        'definitions': Definition,
        'sentences': Sentence,
        'classes': TermClass
    }
    if table_name not in table_to_class:
        return None
    else:
        return session.execute(select(table_to_class[table_name])).all()


def get_term_class(session, name):
    result = session.execute(select(TermClass).where(TermClass.name == name)).first()
    if result is not None:
        return result[0]
    else:
        return None


def get_set(session, name):
    result = session.execute(select(Set).where(Set.name == name)).first()
    if result is not None:
        return result[0]
    else:
        return None


def add_term(session, term, translation, term_class, set, sentences, definitions):
    new_term = Term(term, translation)
    new_term.term_class = term_class
    new_term.set = set
    definitions = [Definition(definition) for definition in definitions]
    sentences = [Sentence(sentence) for sentence in sentences]
    new_term.definitions = definitions
    new_term.sentences = sentences
    session.add(new_term)
    session.commit()


def get_all_terms(session):
    return session.execute(select(Term)).all()


def add_set(session, set_name):
    session.add(Set(set_name))
    session.commit()