from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class FavCity(base):
    __tablename__ = "Favorite Cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer, primary_key=False)
    famous_for = Column(String)


Session = sessionmaker(db)


# opens an actual session by calling the Session() subclass defined above
session = Session()


# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Creating records for our table
istanbul = FavCity(
    name="Istanbul",
    population=25000000,
    famous_for="Worlds Capital"
)

gaziantep = FavCity(
    name="Gaziantep",
    population=2500000,
    famous_for="Best Food"
)


# add each session of our favorite cities to our session
# session.add(istanbul)
session.add(gaziantep)

# Commit each session of our favorite cities to our session
session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# city = session.query(FavCity).filter_by(name=fname).first()
# # defensive programming
# if city is not None:
#     print("City Found: ", city.name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(city)
#         session.commit()
#         print("City has been deleted")
#     else:
#         print("City not deleted")
# else:
#     print("No records found")

# query the data base to find all Cities
myFavCity = session.query(FavCity)
for city in myFavCity:
    print(
        city.id,
        city.name,
        city.population,
        city.famous_for,
        sep=" | "
    )
