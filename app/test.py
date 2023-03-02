#!/usr/bin/python3
from models import storage
storage.new('Voter', {'name': 'ADMIN', 'email': 'admin.com', 'auth_id': 'admin'})
for i in range(2, 51):
    name = 'voter' + str(i)
    email = name + '@student.com'
    storage.new('Voter', {'name': name, 'email': email, 'auth_id': 'admin'})
storage.save()
