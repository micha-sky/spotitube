import pytest
from spotitube import create_spotify_client, get_user_id, get_liked_songs

def test_create_spotify_client():
    sp = create_spotify_client()
    assert sp is not None, "The create_spotify_client function should return a Spotify client"

def test_get_user_id():
    sp = create_spotify_client()
    user_id = get_user_id(sp)
    assert user_id is not None, "The get_user_id function should return a user ID"

def test_get_liked_songs():
    sp = create_spotify_client()
    user_id = get_user_id(sp)
    liked_songs = get_liked_songs(sp, user_id)
    assert liked_songs is not None, "The get_liked_songs function should return a list of liked songs"