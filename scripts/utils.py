import pandas as pd

from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_client(env_file_path: str):
    """
    Reads .env variables and creates a Spotify API client using Spotipy.
    """
    load_dotenv(env_file_path)

    username = os.getenv("USERNAME")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")
    scope = os.getenv("SCOPE")
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username,
                                                   client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))
       
    return sp

def connect_to_database(env_file_path: str):
    load_dotenv(env_file_path)

    database_uri = os.getenv("DATABASE_URI")

    return database_uri

def transform_ms_to_minutes_and_seconds(duration_ms: int) -> pd.DataFrame:
    """
    Transforms the duration of a track from milliseconds to a minute:seconds (mm:ss) format and saves it in a new colum.
    """
    total_seconds = duration_ms/1000
    minutes = int(total_seconds//60)
    seconds = int(total_seconds % 60)
    duration_mm_ss =  f"{minutes:02}:{seconds:02}"
          
    return duration_mm_ss