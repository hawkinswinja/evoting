#!/usr/bin/python3
from sqlalchemy.orm import declarative_base


Base = declarative_base()

from .voter import Voter
from .candidate import Candidate
from .position import Position