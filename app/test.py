#!/usr/bin/python3
from models import storage
storage.new('Voter', {'id':0, 'name':'admin', 'email': 'admin@ikura.com', 'auth_id': 'admin'})
storage.save()
post = storage.all('Voter')
for item in post:
 print(item.name, item.auth_id, item.id)
