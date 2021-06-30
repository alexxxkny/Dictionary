# This file contains means of connecting to databases in order to use them in other modules

from sqlalchemy import create_engine
from sqlalchemy.orm import registry

engine = create_engine('sqlite:///foo.db', echo=False, future=True)
mapper_registry = registry()
Base = mapper_registry.generate_base()
