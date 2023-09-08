import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd


def authenticate_spotify():
    # Spotify Authentication
    spotipy_client_id = "c4fb86c757a840d2bb89db3794af947e"
    spotipy_client_secret = "f9a9ed9a61c747a0ab0fea278c95c4e8"
    spotipy_redirect_uri = "http://127.0.0.1:9090"
    scope = "user-top-read"
    return spotipy_client_id, spotipy_client_secret, spotipy_redirect_uri, scope


def get_track_ids(time_frame):
    track_ids = []
    for song in time_frame["items"]:
        track_ids.append(song["id"])
    return track_ids


def get_track_features(sp, track_id):
    meta = sp.track(track_id)
    # meta
    name = meta["name"]
    album = meta["album"]["name"]
    artist = meta["album"]["artists"][0]["name"]
    spotify_url = meta["external_urls"]["spotify"]
    album_cover = meta["album"]["images"][0]["url"]
    track_info = [name, album, artist, spotify_url, album_cover]
    return track_info


def main():
    client_id, client_secret, redirect_uri, scope = authenticate_spotify()

    # Initiating the sp object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                   redirect_uri=redirect_uri, scope=scope))

    top_tracks_long = sp.current_user_top_tracks()
    track_ids = get_track_ids(top_tracks_long)

    print(get_track_features(sp, track_ids[0]))


if __name__ == "__main__":
    main()

