import os
from letterboxdpy.auth import UserSession

# Logs in if no session exists, or loads the saved session automatically
# session = UserSession.ensure()

# 2. Programmatic login
USER = os.environ.get("LBXD_USERNAME", None)
PWD = os.environ.get("LBXD_PASSWORD", None)
session = UserSession.login(USER, PWD)

# 3. Manual load from custom path
# session = UserSession.load(Path(".cookie/session.json"))

print(f"Authenticated as: {session.username}")
