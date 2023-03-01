#!/usr/bin/python3
from models import storage

voter = storage.show('Voter', 3)
print(voter.name, voter.auth_id)
