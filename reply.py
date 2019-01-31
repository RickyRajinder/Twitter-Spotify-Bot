import streamListener
import tweepy

from settings import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit_notify=True)

Listener = streamListener.StreamListener()
stream = tweepy.Stream(auth=api.auth, listener= Listener)

print("Streaming...")
stream.filter(track=['SpotifySearch', 'spotifysearch', 'SPOTIFYSEARCH', 'spotifySearch', 'SpotifySearch'])

#streamSearch()


#def lambda_handler(_event_json, _context):
 #   streamSearch()

