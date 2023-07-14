from models import storage
import bcrypt
# from models.auth import get_hash

voter = storage.show('Voter', 12)
print(voter.name)
