import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

CONSUMER_KEY=os.getenv("consumer_key")
CONSUMER_SECRET=os.getenv("consumer_secret")

ACCESS_TOKEN=os.getenv("access_token")
ACCESS_TOKEN_SECRET=os.getenv("access_token_secret")