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
