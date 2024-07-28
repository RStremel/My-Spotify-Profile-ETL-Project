from extract import SpotifyExtractor
from transform import SpotifyTransformer
from load import SpotifyLoader

class SpotifyPipeline:
    def __init__(self) -> None:
        self.extract = SpotifyExtractor()
        self.transform = SpotifyTransformer()
        self.load = SpotifyLoader()

    def run_recently_played_pipeline(self):
        self.extract.extract_user_recently_played()
        transformed_data = self.transform.transform_recently_played(raw_json_path='data/raw/recently_played.json')
        self.load.load_to_database(df=transformed_data, table_name="recently_played", if_exists="append")

    def run_top_artists_long_term(self):
        self.extract.extract_top_artists_long_term()
        transformed_data = self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_long_term.json')
        self.load.load_to_database(df=transformed_data, table_name="top_artists_long_term", if_exists="replace")

    def run_top_artists_medium_term(self):
        self.extract.extract_top_artists_medium_term()
        transformed_data = self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_medium_term.json')
        self.load.load_to_database(df=transformed_data, table_name="top_artists_medium_term", if_exists="replace")

    def run_top_artists_short_term(self):
        self.extract.extract_top_artists_short_term()
        transformed_data = self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_short_term.json')
        self.load.load_to_database(df=transformed_data, table_name="top_artists_short_term", if_exists="replace")

    def run_top_tracks_long_term(self):
        self.extract.extract_top_tracks_long_term()
        transformed_data = self.transform.transform_top_tracks(raw_json_path='data/raw/top_tracks_long_term.json')
        self.load.load_to_database(df=transformed_data, table_name="top_tracks_long_term", if_exists="replace")

    def run_top_tracks_medium_term(self):
        self.extract.extract_top_tracks_medium_term()
        transformed_data = self.transform.transform_top_tracks(raw_json_path='data/raw/top_tracks_medium_term.json')
        self.load.load_to_database(df=transformed_data, table_name="top_tracks_medium_term", if_exists="replace")

    def run_top_tracks_short_term(self):
        self.extract.extract_top_tracks_short_term()
        transformed_data = self.transform.transform_top_tracks(raw_json_path='data/raw/top_tracks_short_term.json')
        self.load.load_to_database(df=transformed_data, table_name="top_tracks_short_term", if_exists="replace")
        
    def run_album_tracks_recently_played(self):
        self.extract.extract_album_tracks_recently_played()
        transformed_data = self.transform.transform_album_tracks_recently_played(raw_json_path='data/raw/album_tracks_recently_played.json')
        self.load.load_to_database(df=transformed_data, table_name="album_tracks_recently_played", if_exists="replace")

if __name__ == "__main__":
    pipeline = SpotifyPipeline()
    pipeline.run_recently_played_pipeline()
    pipeline.run_top_artists_long_term()
    pipeline.run_top_artists_medium_term()
    pipeline.run_top_artists_short_term()
    pipeline.run_top_tracks_long_term()
    pipeline.run_top_tracks_medium_term()
    pipeline.run_top_tracks_short_term()
    pipeline.run_album_tracks_recently_played()