from app2 import db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import mapper, sessionmaker, Session

Base = automap_base()
Base.prepare(db, reflect=True)
Employees = Base.classes.employees
session = Session(db)



