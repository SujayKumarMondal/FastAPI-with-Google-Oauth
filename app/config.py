import os
from dotenv import load_dotenv


load_dotenv()

CLIENT_ID = os.environ.get('client-id')
CLIENT_SECRET = os.environ.get('client-secret')
SESSION_SECRET = os.environ.get('session-secret')
