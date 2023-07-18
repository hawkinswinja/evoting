#!/usr/bin/python3
"""this module creates the engine that links to MySQL database"""
from os import getenv
from sqlalchemy.orm import (sessionmaker, scoped_session)
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from models.voter import (Voter, Base)
from models.position import Position
from models.candidate import Candidate


class Engine:
    """alows the perfomance of CRUD operations on the database"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the SQL database"""
        user = getenv('USER')
        host = getenv('HOST')
        pw = getenv('PW')
        db = getenv('DB')
        dbtype = getenv('DT')
        url = f'//{user}:{pw}@{host}/{db}'

        if dbtype == 'mysql':
            self.__engine = create_engine('mysql+mysqldb:' + url)
        else:
            self.__engine = create_engine('postgresql+psycopg2:' + url)

        # map all subclasses of Base to create the database
        Base.metadata.create_all(self.__engine)

    def destroy(self):
        """Destroy the current db and all its contents"""
        Base.metadata.destroy_all()

    def reload(self):
        """reloads all created contents of the database"""
        # create the engine session
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls):
        """returns all instances of object specified in cls"""
        return (self.__session.query(eval(cls)).all())

    def new(self, cls, me=None):
        """
            adds records to the database
            string cls: class name used to create instance object
            dict me: dictionary definition for new object to create
        """
        # do nothing when the dictionary item me is NULL
        if me is None:
            return
        else:
            obj = eval(cls)()
            for k, v in me.items():
                setattr(obj, k, v)
        try:
            self.__session.add(obj)
        except SQLAlchemyError:  # NOT WORKING NEEDS updates!!
            print("Failed to update")

    def save(self):
        """commit changes to database"""
        self.__session.commit()

    def delete(self, cls, id=None):
        """delete an existing record using the primary key"""
        # create object from passed class name
        obj = eval(cls)
        # delete all stored objects if item is missing
        if id is None:
            self.__session.query(obj).delete(synchronize_session=False)
        else:
            # fetch an object using its primary key and delete it
            self.__session.delete(self.show(cls, id))

    def show(self, cls, cls_id):
        """returns an object using the primary key"""
        return (self.__session.query(eval(cls)).get(cls_id))
