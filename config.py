from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("AgCHnR8DMhG33M7v9sAUY6_pNt3pOD6n02Xn7oHcgR5oCaijQhZXUBoY8IwNQibDRs5_77Gvf9_ELSfggOmcI24IP8cWTP1O4ItOGPrqF0f3TCTCIXI4akw6sIhf-e9k7GdjKCGKXUke0IEof9eDN6crrLp6IrnPODCdCHOrdcdFuKwnfXkgDIvpQbl6VIYX_52ZcmJcFt7CPNK_K-CK0VRfJLisdzPlnFmTA8dRlbYmaeKi-unHRi3Pfg00fDgT-D6hew7oewfLqbfDe3feo0MrFmuDC_ij9VMN_FsFf09AcgZnsHqaSO5aEwrQv3OVIw2bAnYkFn6tKnxQDQC7O1nbbk0oJwA", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
