#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()


engine = create_engine("sqlite:///Chinook_Sqlite.sqlite")
Base.prepare(engine, reflect=True)

# Tables

Album = Base.classes.Album
Artist = Base.classes.Artist
Customer = Base.classes.Customer
Employee = Base.classes.Employee
Genre = Base.classes.Genre
Invoice = Base.classes.Invoice
Playlist = Base.classes.Playlist
Track = Base.classes.Track

session = Session(engine)
