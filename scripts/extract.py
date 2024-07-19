from utils import create_client

from datetime import datetime, timedelta
import json

class SpotifyExtractor:
    def __init__(self) -> None:
        self.sp = create_client(env_file_path="config/.env")

    def get_user_recently_played(self):
        """
        Gets info about tracks from the current user's last 50 played tracks in the last 24 hours. 
        """
        yesterday_unix_timestamp = int((datetime.now() - timedelta(days=1)).timestamp())
        return self.sp.current_user_recently_played(limit=None, after=yesterday_unix_timestamp, before=None)

    def get_top_artists_long_term(self):
        """
        Gets the current user's top 50 artists in the long term (calculated from ~1 year of data and 
        including all new data as it becomes available).
        """
        return self.sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')

    def get_top_artists_medium_term(self):
        """
        Gets the current user's top 50 artists in the medium term (approximately last 6 months).
        """
        return self.sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')

    def get_top_artists_short_term(self):
        """
        Gets the current user's top 50 artists in the short term (approximately last 4 weeks).
        """
        return self.sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')

    def get_top_tracks_long_term(self):
        """
        Gets the current user's top 50 tracks in the long term (calculated from ~1 year of data and 
        including all new data as it becomes available).
        """
        return self.sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')

    def get_top_tracks_medium_term(self):
        """
        Gets the current user's top 50 tracks in the medium term (approximately last 6 months).
        """
        return self.sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')

    def get_top_tracks_short_term(self):
        """
        Gets the current user's top 50 tracks in the short term (approximately last 4 weeks).
        """
        return self.sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')

    def get_album_tracks_for_user_recently_played(self):
        """
        Gets Spotify catalog information for the albums, identified by their Spotify IDs, 
        that appear in the last 20 recently played songs.
        """
        album_id_list = []
        album_id_list.extend([track['track']['album']['id'] for track in self.recently_played['items']])
        return self.sp.albums(album_id_list)

    def save_data_to_json_file(self, data, path):
        with open(path, 'w') as f:
            json.dump(data, f)

    def extract_user_recently_played(self):
        self.recently_played = self.get_user_recently_played()
        self.save_data_to_json_file(self.recently_played, 'data/raw/recently_played.json')

    def extract_top_artists_long_term(self):
        self.top_artists_long_term = self.get_top_artists_long_term()
        self.save_data_to_json_file(self.top_artists_long_term, 'data/raw/top_artists_long_term.json')

    def extract_top_artists_medium_term(self):
        self.top_artists_medium_term = self.get_top_artists_medium_term()
        self.save_data_to_json_file(self.top_artists_medium_term, 'data/raw/top_artists_medium_term.json')

    def extract_top_artists_short_term(self):
        self.top_artists_short_term = self.get_top_artists_short_term()
        self.save_data_to_json_file(self.top_artists_short_term, 'data/raw/top_artists_short_term.json')

    def extract_top_tracks_long_term(self):
        self.top_tracks_long_term = self.get_top_tracks_long_term()
        self.save_data_to_json_file(self.top_tracks_long_term, 'data/raw/top_tracks_long_term.json')

    def extract_top_tracks_medium_term(self):
        self.top_tracks_medium_term = self.get_top_tracks_medium_term()
        self.save_data_to_json_file(self.top_tracks_medium_term, 'data/raw/top_tracks_medium_term.json')

    def extract_top_tracks_short_term(self):
        self.top_tracks_short_term = self.get_top_tracks_short_term()
        self.save_data_to_json_file(self.top_tracks_short_term, 'data/raw/top_tracks_short_term.json')

    def extract_album_tracks_for_user_recently_played(self):
        self.album_tracks_recently_played = self.get_album_tracks_for_user_recently_played()
        self.save_data_to_json_file(self.album_tracks_recently_played, 'data/raw/album_tracks_recently_played.json')

if __name__ == "__main__":
    extract = SpotifyExtractor()
    extract.extract_user_recently_played()
    extract.extract_album_tracks_for_user_recently_played()
        

