from models import *
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# CITY OBJECTS
la = City(name='Los Angeles', state='CA')
nyc = City(name='New York City', state='NY')
session.add_all([la, nyc])
session.commit()

# SPORTS OBJECTS
baseball = Sports(name='Baseball')
bball = Sports(name='Basketball')
session.add_all([baseball, bball])
session.commit()

# READING CSVS
la_dodgers = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
la_lakers = pd.read_csv('la_lakers_basketball.csv').to_dict(orient='records')
ny_yankees = pd.read_csv('ny_yankees_baseball.csv').to_dict(orient='records')
ny_knicks = pd.read_csv('ny_knicks_basketball.csv').to_dict(orient='records')

# FUNCTION TO CREATE PLAYERS
def populate_teams(data):
    player_list = []
    for x in data:
        P = Players(name=x.get('name'),age = x.get('age', None),number=x.get('number', None), height=x.get('height',None), weight=x.get('weight', None))
        player_list.append(P)
    return player_list

# SETTING VARIABLES TO OUTCOME OF ABOVE FUNCTION PER TEAM
dodgers_players = populate_teams(la_dodgers)
lakers_players = populate_teams(la_lakers)
yankees_players = populate_teams(ny_yankees)
knicks_players = populate_teams(ny_knicks)

# TEAM OBJECTS
dodgers = Teams(name='Dodgers', city=la, sport=baseball, teams_=dodgers_players)
yankees = Teams(name='NY Yankees', sport=baseball, city=nyc, teams_=yankees_players)
lakers = Teams(name='LA Lakers', sport=bball, city=la, teams_=lakers_players)
knicks = Teams(name='NY Knicks', sport=bball, city=nyc, teams_=knicks_players)

# ADDING & COMMITTING TEAM OBJECTS
session.add_all([dodgers, lakers, yankees, knicks])
session.commit()

# dodgers = Teams(
#     name = 'LA Dodgers',
#     city_id = session.query(City).filter(City.name=='Los Angeles').first().id,
#     sport_id = session.query(Sports).filter(Sports.name=='Baseball').first().id
#     )
#
# lakers = Teams(
#     name = 'LA Lakers',
#     city_id = session.query(City).filter(City.name=='Los Angeles').first().id,
#     sport_id = session.query(Sports).filter(Sports.name=='Basketball').first().id
#     )
#
# knicks = Teams(
#     name = 'NY Knicks',
#     city_id = session.query(City).filter(City.name=='New York City').first().id,
#     sport_id = session.query(Sports).filter(Sports.name=='Basketball').first().id
#     )
#
# yankees = Teams(
#     name = 'NY Yankees',
#     city_id = session.query(City).filter(City.name=='New York City').first().id,
#     sport_id = session.query(Sports).filter(Sports.name=='Baseball').first().id
#     )
