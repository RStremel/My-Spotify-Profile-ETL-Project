from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, date
import pandas as pd
import time
import inspect
from utils import ms_to_minutes_and_seconds

class SpotifyExtraction:
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
        Gets info about tracks from the current user's last 50 played tracks. 
        """
        data = self.sp.current_user_recently_played(limit=50, after=None, before=None)

        self.recently_played_list = [
            {
                'track_id': row['track']['id'],
                'track_name': row['track']['name'],
                'track_length': row['track']['duration_ms'],
                'artist_id': row['track']['artists'][0]['id'],
                'artist_name': row['track']['artists'][0]['name'],
                'artist_url': row['track']['artists'][0]['external_urls']['spotify'],
                'album_id': row['track']['album']['id'],
                'album_name': row['track']['album']['name'],
                'album_release_date': row['track']['album']['release_date'],
                'album_total_tracks': row['track']['album']['total_tracks'],
                'album_url': row['track']['album']['external_urls']['spotify'],
                'played_at': row['played_at'],
            }
            for row in data['items']
        ]
        
        self.create_dataframe_from_list(data = self.recently_played_list, function_name=inspect.currentframe().f_code.co_name)
        self.transform_ms_to_minutes_and_seconds(dataframe=self.dataframe)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("User's 50 recently played tracks obtained.")
        time.sleep(1)

    def get_top_artists_long_term(self) -> pd.DataFrame:
        """
        Gets the current user's top 50 artists in the long term (calculated from ~1 year of data and 
        including all new data as it becomes available).
        """
        data = self.sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')

        top_artists_long_term = [
            {
                'rank': index + 1,
                'artist_id': row['id'],
                'artist_name': row['name'],
                'artist_url': row['external_urls']['spotify'],             
            }
            for index, row in enumerate(data['items'])
        ]
        
        self.create_dataframe_from_list(data = top_artists_long_term, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("The user's 50 most listened to artists in the long term obtained.")
        time.sleep(1)

    def get_top_artists_medium_term(self) -> pd.DataFrame:
        """
        Gets the current user's top 50 artists in the medium term (approximately last 6 months).
        """
        data = self.sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')

        top_artists_medium_term = [
            {
                'rank': index + 1,
                'artist_id': row['id'],
                'artist_name': row['name'],
                'artist_url': row['external_urls']['spotify'],
            }
            for index, row in enumerate(data['items'])
        ]
        
        self.create_dataframe_from_list(data = top_artists_medium_term, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)
    
        print("The user's 50 most listened to artists in the medium term obtained.")
        time.sleep(1)

    def get_top_artists_short_term(self) -> pd.DataFrame:
        """
        Gets the current user's top 50 artists in the short term (approximately last 4 weeks).
        """
        data = self.sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')

        top_artists_short_term = [
            {
                'rank': index + 1,
                'artist_id': row['id'],
                'artist_name': row['name'],
                'artist_url': row['external_urls']['spotify'],
            }
            for index, row in enumerate(data['items'])
        ]
    
        self.create_dataframe_from_list(data = top_artists_short_term, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("The user's 50 most listened to artists in the short term obtained.")
        time.sleep(1)

    def get_top_tracks_long_term(self) -> pd.DataFrame:
        """
        Gets the current user's top 50 tracks in the long term (calculated from ~1 year of data and 
        including all new data as it becomes available).
        """
        data = self.sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')

        top_tracks_long_term = [
            {
                'rank': index + 1,
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']
            }
            for index, row in enumerate(data['items'])
        ]

        self.create_dataframe_from_list(data = top_tracks_long_term, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("The user's 50 most listened to tracks in the long term obtained.")
        time.sleep(1)

    def get_top_tracks_medium_term(self) -> pd.DataFrame:
        """
        Gets the current user's top 50 tracks in the medium term (approximately last 6 months).
        """
        data = self.sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')

        top_tracks_medium_term = [
            {
                'rank': index + 1,
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']
            }
            for index, row in enumerate(data['items'])
        ]

        self.create_dataframe_from_list(data = top_tracks_medium_term, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("The user's 50 most listened to tracks in the medium term obtained.")
        time.sleep(1)

    def get_top_tracks_short_term(self) -> pd.DataFrame:
        """
        Gets the current user's top 50 tracks in the short term (approximately last 4 weeks).
        """
        data = self.sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')

        top_tracks_short_term = [
            {
                'rank': index + 1,
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']
            }
            for index, row in enumerate(data['items'])
        ]

        self.create_dataframe_from_list(data = top_tracks_short_term, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("The user's 50 most listened to tracks in the short term obtained.")
        time.sleep(1)

    def get_album_tracks_for_user_recently_played(self):
        """
        Gets Spotify catalog information for the albums, identified by their Spotify IDs, 
        that appear in the last 20 recently played songs.
        """
        album_id_list = []

        for row in self.recently_played_list:
            album_id_list.append(row['album_id'])
            if len(album_id_list) == 20:
                break

        data = self.sp.albums(album_id_list)

        albums_tracks = [
            {
                'album_id': row['id'],
                'tracks': [track['name'] for track in row['tracks']['items']]
            }
            for row in data['albums']
        ]

        self.create_dataframe_from_list(data = albums_tracks, function_name=inspect.currentframe().f_code.co_name)
        self.create_csv_file(dataframe=self.dataframe, function_name=inspect.currentframe().f_code.co_name)

        print("Tracks from the user's 20 most recently listened to albums retrieved.")
        time.sleep(1)

    def create_dataframe_from_list(self, data: list[dict], function_name: str) -> pd.DataFrame:
        """
        Creates a dataframe from the list of dictionaries created in a given function.
        """
        self.dataframe = pd.DataFrame.from_dict(data)
        self.dataframe["extracted_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if function_name == "get_album_tracks_for_user_recently_played":
            self.dataframe = self.dataframe[~self.dataframe["tracks"].apply(pd.Series).duplicated()]
        else:
            pass
        
        return self.dataframe
    
    def transform_ms_to_minutes_and_seconds(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Iterate through a list of track duration (in milliseconds) and transforms it into a minute:seconds (mm:ss) format.
        """
        dataframe["track_length"] = dataframe["track_length"].apply(lambda x: ms_to_minutes_and_seconds(x))
                
        return self.dataframe
        
    def create_csv_file(self, dataframe: pd.DataFrame, function_name: str):
        """
        Saves the previously created dataframe as .csv file, with its name ending with datetime.now()
        """
        dataframe.to_csv(f"./data/{date.today()}-" + function_name.removeprefix("get_") + ".csv", index=False)

if __name__ == "__main__":
    spotifystuff = SpotifyExtraction()
    spotifystuff.create_auth()
    spotifystuff.get_user_recently_played()
    spotifystuff.get_top_artists_long_term()
    spotifystuff.get_top_artists_medium_term()
    spotifystuff.get_top_artists_short_term()
    spotifystuff.get_top_tracks_long_term()
    spotifystuff.get_top_tracks_medium_term()
    spotifystuff.get_top_tracks_short_term()
    spotifystuff.get_album_tracks_for_user_recently_played()