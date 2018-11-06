from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine

Base = declarative_base()

## BELOW = CREATING MY TABLES
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    state = Column(Text)
    city_ = relationship('Teams')


class Sports(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    sport_ = relationship('Teams')


class Teams(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    teams_ = relationship('Players')

    city_id = Column(Integer, ForeignKey('city.id')) #this one
    city = relationship(City, back_populates='city_')

    sport_id = Column(Integer, ForeignKey('sports.id')) #this one
    sport = relationship(Sports, back_populates='sport_')


class Players(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    number = Column(Integer, default=None)
    height = Column(Text)
    weight = Column(Float)
    age = Column(Text)
    team_id = Column(Integer, ForeignKey('teams.id')) # this one
    team = relationship(Teams, back_populates='teams_')


##### BELOW = INSTANTIATING MY OBJECTS
# engine = create_engine('sqlite:///sports.db')
# Base.metadata.create_all(engine)
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# nyc = City(name='New York City', state='New York')
# la = City(name='Los Angeles', state='California' )
#
# bball = Sports(name='Basketball')
# baseball = Sports(name='Baseball')
#
# session.add_all([la,nyc,bball,baseball])
# session.commit()
