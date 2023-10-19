from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()


engine = create_engine("sqlite:///Chinook_Sqlite.sqlite")
Base.prepare(engine, reflect=True)

# Tables

album = Base.classes.Album
artist = Base.classes.Artist
customer = Base.classes.Customer

session = Session(engine)