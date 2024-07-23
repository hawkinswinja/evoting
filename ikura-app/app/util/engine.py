#!/usr/bin/python3
"""this module creates the engine that links to the database"""
from os import getenv
from sqlalchemy.orm import (sessionmaker, scoped_session)
from sqlalchemy import create_engine
from app.models import (Base, Candidate, Position, Voter)

# url = 'engine//ikura:ikura@postgres-container:5432/postgres'


class Engine:
    """Allows the perfomance of CRUD operations on the database"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the database"""
        user = getenv('POSTGRES_USER', 'ikura')
        host = getenv('POSTGRES_HOST', 'localhost')
        port = getenv('POSTGRES_PORT', '5432')
        pw = getenv('POSTGRES_PASSWORD', 'ikura')
        db = getenv('POSTGRES_DB', 'ikura')
        url = '//{}:{}@{}:{}/{}'.format(user, pw, host, port, db)

        self.class_map = {
            'Candidate': Candidate,
            'Position': Position,
            'Voter': Voter
        }

        # if dbtype == 'mysql':
        #     port = getenv('DB_PORT', '3306')
        #     self.__engine = create_engine('mysql+mysqldb:' + url)
        # else:
        self.__engine = create_engine('postgresql+psycopg2:' + url)

        # map all subclasses of Base to create the database
        Base.metadata.create_all(self.__engine)

    def destroy(self):
        """Destroy the current db and all its contents"""
        Base.metadata.drop_all(bind=self.__engine)

    def reload(self):
        """reloads all created contents of the database"""
        # create the engine session
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls):
        """returns all instances of object specified in cls"""
        class_obj = self.class_map.get(cls)
        if class_obj:
            return self.__session.query(class_obj).all()
        else:
            raise ValueError(f"Class {cls} not found")

    def new(self, cls, me=None):
        """
            adds records to the database
            string cls: class name used to create instance object
            dict me: dictionary definition for new object to create
        """
        if me is None:
            raise ValueError("Dictionary item is missing")
        else:
            class_obj = self.class_map.get(cls)
            if class_obj:
                obj = class_obj()
                for k, v in me.items():
                    setattr(obj, k, v)
                try:
                    self.__session.add(obj)
                except Exception:
                    self.__session.rollback()
            else:
                raise ValueError(f"Class {cls} not found")

    def save(self):
        """commits the changes to database"""
        self.__session.commit()

    def delete(self, cls, id=None):
        """delete an existing record using the primary key"""
        # create object from passed class name
        class_obj = self.class_map.get(cls)
        if class_obj:
            if id is None:
                self.__session.query(class_obj).delete(synchronize_session=False)
            else:
                obj = self.__session.get(class_obj, id)
                if obj:
                    self.__session.delete(obj)
        else:
            raise ValueError(f"Class {cls} not found")

    def show(self, cls, cls_id):
        """returns an object using the primary key"""
        class_obj = self.class_map.get(cls)
        if class_obj:
            try:
                return self.__session.get(class_obj, cls_id)
            except Exception:
                raise Exception("Error: Object not found")
        else:
            raise ValueError(f"Class {cls} not found")
