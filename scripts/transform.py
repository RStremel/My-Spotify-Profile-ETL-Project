import json
from datetime import datetime
import pandas as pd

from utils import transform_ms_to_minutes_and_seconds

class SpotifyTransformer:
    def __init__(self) -> None:
        pass

    def transform_recently_played(self, raw_json_path):
        with open(raw_json_path) as f:
            recently_played = json.load(f)

        processed_recently_played = [
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
            for row in recently_played['items']
        ]

        self.df = pd.DataFrame(processed_recently_played)
        self.df["extracted_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.df["track_length"] = self.df["track_length"].apply(lambda x: transform_ms_to_minutes_and_seconds(x))
        return self.df
    
    def transform_top_artists(self, raw_json_path):
        with open(raw_json_path) as f:
            top_artists = json.load(f)

        processed_top_artists = [
            {
                'rank': index + 1,
                'artist_id': row['id'],
                'artist_name': row['name'],
                'artist_url': row['external_urls']['spotify'],             
            }
            for index, row in enumerate(top_artists['items'])
        ]
        
        df = pd.DataFrame(processed_top_artists)
        df["extracted_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return self.df
    
    def transform_top_tracks(self, raw_json_path):
        with open(raw_json_path) as f:
            top_tracks = json.load(f)

        processed_top_tracks = [
            {
                'rank': index + 1,
                'track_id': row['id'],
                'track_name': row['name'],
                'track_artist': row['artists'][0]['name']         
            }
            for index, row in enumerate(top_tracks['items'])
        ]
        
        df = pd.DataFrame(processed_top_tracks)
        df["extracted_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return self.df
    
    def transform_album_tracks_recently_played(self, raw_json_path):
        with open(raw_json_path) as f:
            albums_tracks = json.load(f)

        processed_albums_tracks = [
            {
                'album_id': row['id'],
                'tracks': [track['name'] for track in row['tracks']['items']]
            }
            for row in albums_tracks['albums']
        ]
        
        df = pd.DataFrame(processed_albums_tracks)
        df["extracted_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return self.df

# if __name__ == "__main__":
#     t = SpotifyTransformer()
#     dft = t.transform_recently_played(raw_json_path='data/raw/recently_played.json')

# #     dfartlt = t.transform_top_artists(raw_json_path='data/raw/top_artists_long_term.json')
# #     dfartmt = t.transform_top_artists(raw_json_path='data/raw/top_artists_medium_term.json')
# #     dfartst = t.transform_top_artists(raw_json_path='data/raw/top_artists_short_term.json')


#     dft.to_csv('data/gold/dft.csv', index=False)
# #     dfartlt.to_csv('data/gold/top_artists_long_term.csv', index=False)
# #     dfartmt.to_csv('data/gold/top_artists_medium_term.csv', index=False)
# #     dfartst.to_csv('data/gold/top_artists_short_term.csv', index=False)