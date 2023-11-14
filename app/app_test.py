from models import storage, auth

storage.new('Voter', {'name': 'admin', 'email': 'admin@ikura',
                      'auth_id': auth.get_hash('admin23').decode()})
for i in range(5):
    name = 'student' + str(i)
    email = name + '@email.com'
    pw = auth.get_hash('pw' + name).decode()
    storage.new('Voter', {'name': name, 'email': email, 'auth_id': pw})
storage.save()
users = storage.all('Voter')
if len(users) == 5:
  print('Tests Passed')
else:
  print('Failed tests')
