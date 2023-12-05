#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

engine = create_engine('your_database_connection_string')  # Replace with your database connection string
Session = sessionmaker(bind=engine)
session = Session()


session.query(Game).delete()
session.commit()

fake = Faker()

print("Seeding games...")

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=fake.random_int(min=0, max=60)
    )
    for i in range(50)
]

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
