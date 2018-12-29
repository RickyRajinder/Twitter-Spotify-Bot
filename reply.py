import tweepy
import spotipy
import spotipy.oauth2 as oauth2

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

credentials = oauth2.SpotifyClientCredentials(
	client_id='000bbd9b28c64545a3afa3e1356bee4a',
	client_secret='4314837db2434871bc84e75451d972de'
)
token = credentials.get_access_token()
spotipy = spotipy.Spotify(auth=token)

#birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

#results = spotipy.artist_albums(birdy_uri, album_type='album')
#albums = results['items']
#while results['next']:
 #   results = spotipy.next(results)
  #  albums.extend(results['items'])

#for album in albums:
 #   print(album['name'])

twt = api.search(q="@SpotifySearch")

txt = ['@SpotifySearch',
	   '@spotifysearch',
	   '@spotifySearch',
	   '@Spotifysearch']

with open('temp.txt', 'w') as f:
	for tweet in twt:
		f.write(tweet.user.screen_name + '\t')
		f.write('{}\n'.format(tweet.text))

for st in twt:
	for s in txt:
		if s == st.text:
			tweetTxt = st.text
			print(tweetTxt)
			usr = st.user.screen_name
			msg = ("@%s Hello" % (usr))
		#	st = api.update_status(msg, st.id)

spotifyRes = spotipy.search('track:Taki taki', limit=1, offset=0, type='track')
print(spotifyRes['tracks']['items'][0]['external_urls'])