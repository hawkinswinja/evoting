from .engine import Engine
from .auth import (validate, get_hash)


storage = Engine()
storage.reload()