import tweepy
import spotipy
import spotipy.oauth2 as oauth2

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

credentials = oauth2.SpotifyClientCredentials(client_id='000bbd9b28c64545a3afa3e1356bee4a',
    client_secret='4314837db2434871bc84e75451d972de')
token = credentials.get_access_token()
spotipy = spotipy.Spotify(auth=token)


twt = api.search(q="@SpotifySearch")

txt = ['@SpotifySearch', '@spotifysearch', '@spotifySearch', '@Spotifysearch']

with open('temp.txt', 'w') as f:
    for tweet in twt:
        f.write(tweet.user.screen_name + '\t')
        f.write('{}\n'.format(tweet.text))

for st in twt:
    tweetTxt = st.text.lower()
    tweetTxt = tweetTxt.replace('@spotifysearch', '')
    usr = st.user.screen_name
    print(tweetTxt)
    if len(tweetTxt) <= 1:
        msg = ("@%s Hello, I couldn't find a track with your specified criteria. Please be more specific :)" % (usr))
        try:
            st = api.update_status(msg, st.id)
        except tweepy.error.TweepError:
            pass
        continue
    searchCriteria = 'track: ' + tweetTxt
    print(searchCriteria)
    spotifyRes = spotipy.search(searchCriteria, limit=1, offset=0, type='track')
    spotifyRes = spotifyRes['tracks']['items'][0]['external_urls']
    link = spotifyRes.get('spotify')
    print(link)
    msg = ("@%s Hello, I found this track: " % (usr))
    msg = msg + link
    try:
        st = api.update_status(msg, st.id)
    except tweepy.error.TweepError:
        pass
