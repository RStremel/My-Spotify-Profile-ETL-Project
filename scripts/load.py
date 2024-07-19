from sqlalchemy import create_engine
import sqlite3
import pandas as pd

class SpotifyLoader:
    def __init__(self) -> None:
        self.database_uri = "postgresql://username:password@localhost/dbname"
        # self.engine = create_engine(self.database_uri, echo=False)
        # self.conn = sqlite3.connect("spotifydb.db")

    def load_recently_played(self, df):
        engine = create_engine(self.database_uri)
        df.to_sql("recently_played", engine, if_exists="append", index=False)

    def load_top_artists_long_term(self, df):
        self.engine = create_engine(self.database_uri, echo=False)
        df.to_sql("top_artists_long_term", engine=self.engine, if_exists="replace", index=False)

    def load_top_artists_medium_term(self, df):
        self.engine = create_engine(self.database_uri, echo=False)
        df.to_sql("top_artists_medium_term", engine=self.engine, if_exists="replace", index=False)

    def load_top_artists_short_term(self, df):
        self.engine = create_engine(self.database_uri, echo=False)
        df.to_sql("top_artists_short_term", engine=self.engine, if_exists="replace", index=False)

    def load_top_tracks_long_term(self, df):
        self.engine = create_engine(self.database_uri, echo=False)
        df.to_sql("top_tracks_long_term", engine=self.engine, if_exists="replace", index=False)

    def load_top_tracks_medium_term(self, df):
        self.engine = create_engine(self.database_uri, echo=False)
        df.to_sql("top_tracks_medium_term", engine=self.engine, if_exists="replace", index=False)

    def load_top_tracks_short_term(self, df):
        self.engine = create_engine(self.database_uri, echo=False)
        df.to_sql("top_tracks_short_term", engine=self.engine, if_exists="replace", index=False)

    def load_album_tracks_recently_played(self, df):
        df.to_sql("album_tracks_recently_played", engine=self.engine, if_exists="replace", index=False)
