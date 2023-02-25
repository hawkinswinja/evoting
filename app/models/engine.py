#!/usr/bin/python3
"""this module creates the engine that links to MySQL database"""
from sqlalchemy.orm import (sessionmaker, scoped_session)
from sqlalchemy import create_engine
from models.voter import (Voter, Base)
from models.position import Position
from models.candidate import Candidate


class Engine:
    """alows the perfomance of CRUD operations on the database"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the SQL database"""
        self.__engine = create_engine('mysql+mysqldb://root:root@localhost/evoting')
        Base.metadata.create_all(self.__engine)

    def reload(self):
        """reloads all created contents of the database"""
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls):
        """returns all instances of object specified in cls"""
        return(self.__session.query(eval(cls)).all())

    def new(self, cls, me=None):
        """adds records to the database"""
        if me is None:
            return
        else:
            obj = eval(cls)()
            for k, v in me.items():
                setattr(obj, k, v)
            self.__session.add(obj)

    def save(self):
        """commit changes to database"""
        self.__session.commit()

    def delete(self, cls, item=None):
        """delete an existing record"""
        obj = eval(cls)
        if item is None:
            self.__session.query(obj).delete(synchronize_session=False)
        else:
            self.__session.delete(self.show(cls, item))

    def show(self, cls, cls_id):
        """returns an object from database items"""
        return (self.__session.query(eval(cls)).get(cls_id))
