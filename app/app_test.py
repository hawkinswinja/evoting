from models import storage, auth

storage.new('Voter', {'name': 'admin', 'email': 'admin@ikura',
                      'auth_id': auth.get_hash('admin23').decode()})
for i in range(2, 26):
    name = 'student' + str(i)
    email = name + '@email.com'
    pw = auth.get_hash('pw' + name).decode()
    storage.new('Voter', {'name': name, 'email': email, 'auth_id': pw})
storage.save()
users = storage.all('Voter')
for user in users:
    print(user.id, user.name, user.status)
