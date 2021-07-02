from sqlalchemy import create_engine, text, Column, String, Integer, select
from sqlalchemy.orm import Session, registry

engine = create_engine('sqlite:///foo.db', echo=True, future=True)
mapper_registry = registry()
Base = mapper_registry.generate_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f'{self.name} is {self.age} years old'


mapper_registry.metadata.create_all(engine)

with Session(engine) as session:
    user1 = User(name='alex', age=19)
    user2 = User(name='alakey', age=16)
    session.add_all((user1, user2))
    session.commit()
    users = session.execute(select(User)).all()
    for user in users:
        print(user)
        # classes = [TermClass(name='verb'), TermClass(name='noun'), TermClass(name='adjective')]
        # session.add_all(classes)
        # sets = [Set(name='general'), Set(name='environment')]
        # session.add_all(sets)
        # terms = [Term(term='towel', translation='полотенце'),
        #          Term(term='medicine', translation='лекарство'),
        #          Term(term='smooth', translation='гладкий'),
        #          Term(term='bundle', translation='связывать, связка, пучок'),
        #          Term(term='kettle', translation='чайник')]
        # session.add_all(terms)
        # sentences = [Sentence(sentence='You have a such smooth skin!'),
        #              Sentence(sentence='I have two towels.'),
        #              Sentence(sentence='Full the kettle, I wanna have some tea.'),
        #              Sentence(sentence='There is a little water in the kettle, turn it on.')]
        #
        # terms[0].term_class = classes[1]
        # terms[1].term_class = classes[1]
        # terms[2].term_class = classes[2]
        # terms[3].term_class = classes[0]
        # terms[4].term_class = classes[1]
        #
        # print(terms[0].term_class)
        #
        # terms[2].sentences = [sentences[0]]
        # terms[0].sentences = [sentences[1]]
        # terms[4].sentences = [sentences[2], sentences[3]]
        #
        # towel_definition = Definition(definition='thing making your hands dry')
        # towel_definition.term_class = classes[1]
        # terms[0].definitions = [towel_definition]
        #
        # bundle_definition_noun = Definition(definition='multiple things tied together')
        # bundle_definition_verb = Definition(definition='to tie together for carrying or storing')
        # terms[3].definitions = [bundle_definition_noun, bundle_definition_verb]
        #
        # sets[0].terms = [terms[0], terms[1], terms[4]]
        # sets[1].terms = [terms[2], terms[3]]
        #
        # session.commit()
        #
        # print('---------CLASSES----------')
        # for term_class in session.execute(select(TermClass)).all():
        #     print(term_class)
        #     print()
        #
        # print('---------TERMS-----------')
        # for term in session.execute(select(Term)).all():
        #     print(term[0])
        #     print(term[0].term_class)
        #     print(term[0].set)
        #     for sentence in term[0].sentences:
        #         print(sentence)
        #     for definition in term[0].definitions:
        #         print(definition)
        #     print()
        #
        # print('---------------SENTENCES------------------')
        # for sentence in session.execute(select(Sentence)).all():
        #     print(sentence[0])
        #     print(sentence[0].term)
        #     print()
        #
        # print('---------------SETS-------------------')
        # for set in session.execute(select(Set)).all():
        #     print(set[0])
        #     for term in set[0].terms:
        #         print(term)
        #     print()