from app.util import storage, validate, get_hash

admin =  {'name': 'admin', 'email': 'admin@ikura', 'is_admin': True, 'auth_id': get_hash('password').decode()}
storage.new('Voter', admin)

for i in range(2, 10):
    name = 'student' + str(i)
    email = name + '@ikura'
    pw = get_hash(email).decode()
    storage.new('Voter', {'name': name, 'email': email, 'auth_id': pw})
    
storage.save()

students = storage.all('Voter')
for student in students:
    print(student.name, student.email, student.status, student.is_admin)