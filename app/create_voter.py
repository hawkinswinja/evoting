from models import storage
from models.auth import get_hash

'''
for i in range(2, 25):
    name = 'student' + str(i)
    email = name + '@email.sc'
    pw = get_hash('pw@' + name).decode()
    storage.new('Voter', {'name': name, 'email': email, 'status': "Not", 'auth_id': pw})

storage.new('Voter',
            {'name': 'student25', 'email': 'student25@email.sc', 'status': "voted", 'auth_id': get_hash('pw@' + 'student25').decode()})
storage.save()
'''
users = storage.all('Voter')
for user in users:
    print(user.id, user.name, user.email, user.status, user.auth_id)
