import tweepy
import spotipy
import spotipy.oauth2 as oauth2

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit_notify=True)

credentials = oauth2.SpotifyClientCredentials=(client_id,client_secret)
token = credentials.get_access_token()
spotipy = spotipy.Spotify(auth=token)

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        text = status.text
        usr = status.user.screen_name
        id_str = status.id_str
        if hasattr(status, 'retweeted_status'):
            return
        tweetTxt = text.lower()
        tweetTxt = tweetTxt.replace('@spotifysearch', '')
        print("@" + usr + ": " + tweetTxt)
        if len(tweetTxt) <= 1:
            print("Nothing to search")
            msg = (
            "@%s Hello, I couldn't find a track with your specified criteria. Please be more specific \U0001f604" % (usr))
            try:
                api.update_status(msg, id_str)
            except tweepy.error.TweepError:
                pass
            return
        searchCriteria = 'track: ' + tweetTxt
        print(searchCriteria)
        spotifyRes = spotipy.search(searchCriteria, limit=1, offset=0, type='track')
        print(spotifyRes)
        if spotifyRes['tracks']['total'] == 0:
            print('NADA')
            msg = (
                "@%s Hello, I couldn't find anything on Spotify with your specified criteria. Sorry \U0001f604" % (usr))
            try:
                api.update_status(msg, id_str)
            except tweepy.error.TweepError:
                pass
            return
        spotifyRes = spotifyRes['tracks']['items'][0]['external_urls']
        link = spotifyRes.get('spotify')
        print(link)
        msg = ("@%s Hello, I found this track: " % (usr))
        msg = msg + link
        try:
            api.update_status(msg, id_str)
        except tweepy.error.TweepError:
            pass

    def on_error(self, status_code):
        if status_code == 420:
            return False

