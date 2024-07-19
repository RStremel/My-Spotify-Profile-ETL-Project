import pip
from extract import SpotifyExtractor
from transform import SpotifyTransformer
from load import SpotifyLoader

class Pipeline:
    def __init__(self) -> None:
        self.extract = SpotifyExtractor()
        self.transform = SpotifyTransformer()
        self.load = SpotifyLoader()

    def run_recently_played_pipeline(self):
        self.extract.extract_user_recently_played()
        transformed_data = self.transform.transform_recently_played(raw_json_path='data/raw/recently_played.json')
        transformed_data
        # self.load.load_recently_played(df = transformed_data)

    def run_top_artists_short_term(self):
        self.extract.extract_top_artists_short_term()
        transformed_data = self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_short_term.json')
        transformed_data
        

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run_recently_played_pipeline()
    pipeline.run_top_artists_short_term()






 
        
    #     self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_long_term.json')
    #     self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_medium_term.json')
    #     self.transform.transform_top_artists(raw_json_path='data/raw/top_artists_short_term.json')
    #     self.transform.transform_top_tracks(raw_json_path='data/raw/top_tracks_long_term.json')
    #     self.transform.transform_top_tracks(raw_json_path='data/raw/top_tracks_medium_term.json')
    #     self.transform.transform_top_tracks(raw_json_path='data/raw/top_tracks_short_term.json')
    #     self.transform.transform_album_tracks_recently_played(raw_json_path='data/raw/album_tracks_recently_played.json')

    #     self.load.load_recently_played(df=self.df)

    #     def load_recently_played(self, df):
    #     df.to_sql("recently_played", engine=self.engine, if_exists="append", index=False)

    # def load_top_artists_long_term(self, df):
    #     self.engine = create_engine(self.database_uri, echo=False)
    #     df.to_sql("top_artists_long_term", engine=self.engine, if_exists="replace", index=False)

    # def load_top_artists_medium_term(self, df):
    #     self.engine = create_engine(self.database_uri, echo=False)
    #     df.to_sql("top_artists_medium_term", engine=self.engine, if_exists="replace", index=False)

    # def load_top_artists_short_term(self, df):
    #     self.engine = create_engine(self.database_uri, echo=False)
    #     df.to_sql("top_artists_short_term", engine=self.engine, if_exists="replace", index=False)

    # def load_top_tracks_long_term(self, df):
    #     self.engine = create_engine(self.database_uri, echo=False)
    #     df.to_sql("top_tracks_long_term", engine=self.engine, if_exists="replace", index=False)

    # def load_top_tracks_medium_term(self, df):
    #     self.engine = create_engine(self.database_uri, echo=False)
    #     df.to_sql("top_tracks_medium_term", engine=self.engine, if_exists="replace", index=False)

    # def load_top_tracks_short_term(self, df):
    #     self.engine = create_engine(self.database_uri, echo=False)
    #     df.to_sql("top_tracks_short_term", engine=self.engine, if_exists="replace", index=False)

    # def load_album_tracks_recently_played(self, df):
    #     df.to_sql("album_tracks_recently_played", engine=self.engine, if_exists="replace", index=False)

