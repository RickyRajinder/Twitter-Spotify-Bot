import streamListener
import tweepy

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit_notify=True)

Listener = streamListener.StreamListener()
stream = tweepy.Stream(auth=api.auth, listener= Listener)

stream.filter(track=['SpotifySearch', 'spotifysearch', 'SPOTIFYSEARCH', 'spotifySearch', 'SpotifySearch'])
