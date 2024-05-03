import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# create a Spotify API client using Spotipy library
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://localhost/",
                                               scope="user-library-read"
                                               ))

# get the user's ID
user_id = sp.me()['id']

# find the "Liked Songs" playlist ID for the user
playlists = sp.user_playlists(user_id)
tracks = sp.current_user_saved_tracks(limit=50, offset=0)

liked_songs = []
songs = tracks["items"]  # set songs to be the songs from the initial page of data
while tracks["next"]:  # user-playlist response says there are still pages left
    tracks = sp.next(tracks)
    # sp.next is a utility method Spotipy provides
    for item in tracks["items"]:
        songs.append(item)
        name = item['track']['name']
        artist = item['track']['artists'][0]['name']
        liked_songs.append((artist, name))

print(songs)

