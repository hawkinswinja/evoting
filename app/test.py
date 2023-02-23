#!/usr/bin/python3
from models import storage
n = int('36')
user = storage.show('Voter', n)
print(user.name, user.auth_id)
