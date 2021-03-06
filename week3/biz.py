from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os


auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)
