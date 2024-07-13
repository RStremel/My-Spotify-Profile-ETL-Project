from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, date
import pandas as pd
import time
import inspect

class SpotifyStuff:

    def __init__(self):
        load_dotenv()

        self.username = os.getenv("USERNAME")
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.redirect_uri = os.getenv("REDIRECT_URI")
        self.scope = "user-read-recently-played user-top-read"

    def create_auth(self):
        print("Initializing connection to the Spotify API...")
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=self.username,
                                                            client_id=self.client_id,
                                                            client_secret=self.client_secret,
                                                            redirect_uri=self.redirect_uri,
                                                            scope=self.scope))
        
        time.sleep(1)
        
        return self.sp
        
    def get_user_recently_played(self) -> pd.DataFrame:
        """
        Get info about tracks from the current user's last 50 played tracks. 
        """
        data = self.sp.current_user_recently_played(limit=50, after=None, before=None)

        self.recently_played_list = [
            {
                'artist_id': row['track']['artists'][0]['id'],
                'artist_name': row['track']['artists'][0]['name'],
                'artist_url': row['track']['artists'][0]['external_urls']['spotify'],
                'album_id': row['track']['album']['id'],
                'album_name': row['track']['album']['name'],
                'album_release_date': row['track']['album']['release_date'],
                'album_total_tracks': row['track']['album']['total_tracks'],
                'album_url': row['track']['album']['external_urls']['spotify'],
                'track_id': row['track']['id'],
                'track_name': row['track']['name'],
                'track_length': row['track']['duration_ms'],
                'played_at': row['played_at'],
            }
            for row in data['items']
        ]

        self.create_csv_file(data=self.recently_played_list, function_name=inspect.currentframe().f_code.co_name)

        print("User's recently played tracks obtained.")
        time.sleep(1)

        return self.recently_played_list

    def get_top_artists_long_term(self) -> pd.DataFrame:
        """
        Get the current user's top 50 artists in the long term (calculated from ~1 year of data and 
        including all new data as it becomes available).
        """
        data = self.sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')

        top_artists_long_term = [
            {
                'artist_id': row['id'],
                'artist_url': row['external_urls']['spotify'],
                'artist_name': row['name']
            }
            for row in data['items']
        ]
    
        self.create_csv_file(data=top_artists_long_term, function_name=inspect.currentframe().f_code.co_name)

        print("User's top 50 artists in the long term obtained.")
        time.sleep(1)

    def get_top_artists_medium_term(self) -> pd.DataFrame:
        """
        Get the current user's top 50 artists in the medium term (approximately last 6 months).
        """
        data = self.sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')

        top_artists_medium_term = [
            {
                'artist_id': row['id'],
                'artist_url': row['external_urls']['spotify'],
                'artist_name': row['name']
            }
            for row in data['items']
        ]
    
        self.create_csv_file(data=top_artists_medium_term, function_name=inspect.currentframe().f_code.co_name)

        print("User's top 50 artists in the medium term obtained.")
        time.sleep(1)

    def get_top_artists_short_term(self) -> pd.DataFrame:
        """
        Get the current user's top 50 artists in the short term (approximately last 4 weeks).
        """
        data = self.sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')

        top_artists_short_term = [
            {
                'artist_id': row['id'],
                'artist_url': row['external_urls']['spotify'],
                'artist_name': row['name']
            }
            for row in data['items']
        ]
    
        self.create_csv_file(data=top_artists_short_term, function_name=inspect.currentframe().f_code.co_name)

        print("User's top 50 artists in the short term obtained.")
        time.sleep(1)

    def get_top_tracks_long_term(self) -> pd.DataFrame:
        """
        Get the current user's top 50 tracks in the long term (calculated from ~1 year of data and 
        including all new data as it becomes available).
        """
        data = self.sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')

        top_tracks_long_term = [
            {
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']
            }
            for row in data['items']
        ]

        self.create_csv_file(data=top_tracks_long_term, function_name=inspect.currentframe().f_code.co_name)

        print("User's top 50 tracks in the long term obtained.")
        time.sleep(1)

    def get_top_tracks_medium_term(self) -> pd.DataFrame:
        """
        Get the current user's top 50 tracks in the medium term (approximately last 6 months).
        """
        data = self.sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')

        top_tracks_medium_term = [
            {
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']
            }
            for row in data['items']
        ]

        self.create_csv_file(data=top_tracks_medium_term, function_name=inspect.currentframe().f_code.co_name)

        print("User's top 50 tracks in the medium term obtained.")
        time.sleep(1)

    def get_top_tracks_short_term(self) -> pd.DataFrame:
        """
        Get the current user's top 50 tracks in the short term (approximately last 4 weeks).
        """
        data = self.sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')

        top_tracks_short_term = [
            {
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']
            }
            for row in data['items']
        ]

        self.create_csv_file(data=top_tracks_short_term, function_name=inspect.currentframe().f_code.co_name)

        print("User's top 50 tracks in the short term obtained.")
        time.sleep(1)

    def get_album_info_for_user_recently_played(self):
        """
        Get Spotify catalog information for the albums, identified by their Spotify IDs, 
        that contain the last 20 recently played songs.
        """
        album_id_list = []

        for row in self.recently_played_list:
            album_id_list.append(row['album_id'])
            if len(album_id_list) == 20:
                break

        data = self.sp.albums(album_id_list)

        albums_info = [
            {
                'album_id': row['id'],
                'album_name': row['name'],
                'tracks': [track['name'] for track in row['tracks']['items']],
                'total_tracks': row['total_tracks'],
                'album_release_date': row['release_date'],
                'album_artist': [artist['name'] for artist in row['artists']],
                'genres': row['genres']
            }
            for row in data['albums']
        ]

        self.create_csv_file(data=albums_info, function_name=inspect.currentframe().f_code.co_name)

        print("Album info for user's recently played tracks obtained.")
        time.sleep(1)

    def create_csv_file(self, data: list[dict], function_name: str):
        """
        Create a dataframe from the list of dictionaries created in a given function
        and then saves it as .csv file, with the name ending with datetime.now()"""
        dataframe = pd.DataFrame.from_dict(data)
        dataframe["extracted_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        dataframe.to_csv(f"data/{date.today()}-" + function_name.removeprefix("get_") + ".csv")

if __name__ == "__main__":
    spotifystuff = SpotifyStuff()
    spotifystuff.create_auth()
    spotifystuff.get_user_recently_played()
    spotifystuff.get_top_artists_long_term()
    spotifystuff.get_top_artists_medium_term()
    spotifystuff.get_top_artists_short_term()
    spotifystuff.get_top_tracks_long_term()
    spotifystuff.get_top_tracks_medium_term()
    spotifystuff.get_top_tracks_short_term()
    spotifystuff.get_album_info_for_user_recently_played()