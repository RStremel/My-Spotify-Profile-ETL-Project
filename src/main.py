import os
from dotenv import load_dotenv
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = "user-read-recently-played user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

recently_played = sp.current_user_recently_played(limit=50, after=None, before=None)

# top_artists_long_term = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
# top_artists_medium_term = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
# top_artists_short_term = sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')

def get_recently_played_info(recently_played_data: dict) -> list[dict]:
    """
    ADD+++++++++++++++++++++++++++++++++++++++++++ 
    """
    recently_played_list = [
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
        for row in recently_played_data['items']
    ]

    return recently_played_list



### funções para retornar as mais ouvidas - 4 semanas, 6 meses, 12 meses

 

### funções pra retornar informações do artista/album/track da listagem das 50 recentemente ouvidas


def generate_df_from_recently_played_list(recently_played_list: list[dict]) -> pd.DataFrame:
    """
    ADD+++++++++++++++++++++++++++++++++++++++++++ 
    """
    recently_played_df = pd.DataFrame.from_dict(recently_played_list)

    return recently_played_df



recently_played_list = get_recently_played_info(recently_played)

recently_played_df = generate_df_from_recently_played_list(recently_played_list)

# recently_played_df.to_csv('data.csv', encoding='utf-8')

print(recently_played_df)





# def get_album_info(data):
#     album_list = [
#         {
#             'album_id': row['track']['album']['id'],
#             'album_name': row['track']['album']['name'],
#             'album_release_date': row['track']['album']['release_date'],
#             'album_total_tracks': row['track']['album']['total_tracks'],
#             'album_url': row['track']['album']['external_urls']['spotify']
#         }
#         for row in data['items']
#     ]

#     album_df = pd.DataFrame.from_dict(album_list)

#     print(f"--- {time.time()} seconds ---")

#     print(album_df)
#     return album_df

# album_df = get_album_info(recently_played)








# if recently_played_df.empty:
#     print("Nenhuma música escutada ")





# album_name = most_played['items'][0]['track']['album']['name']
# album_id = most_played['items'][0]['track']['album']['id']
# album_release_date = most_played['items'][0]['track']['album']['release_date']
# track_length = most_played['items'][0]['track']['duration_ms']
# track_id = most_played['items'][0]['track']['id']
# track_name = most_played['items'][0]['track']['name']
# played_at = most_played['items'][0]['context']



# playlist_link = "https://open.spotify.com/playlist/0emV5saNMkpbDBcYQYeTwq"

# playlist_URI = playlist_link.split("/")[-1].split('?')[0]

# # LOOP A CADA OFFSET=100+100 ATÉ DF SER VAZIO
# data = sp.playlist_tracks(playlist_URI, offset=0, market="US")

# # album_list = []
# # for row in data['items']:
# #     album_id = row['track']['album']['id']
# #     album_name = row['track']['album']['name']
# #     album_release_date = row['track']['album']['release_date']
# #     album_total_tracks = row['track']['album']['total_tracks']
# #     album_url = row['track']['album']['external_urls']['spotify']
# #     album_element = {'album_id':album_id,'name':album_name,'release_date':album_release_date,
# #                         'total_tracks':album_total_tracks,'url':album_url}
# #     album_list.append(album_element)



# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])



# def get_auth_token():
#     client_creds = client_id + ":" + client_secret
#     client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

#     url = "https://accounts.spotify.com/api/token"

#     headers = {
#         "Authorization": f"Basic {client_creds_b64}",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "redirect_uri": "http://localhost",
#         "scope": "user-top-read"
#     }

#     data = {"grant_type": "client_credentials"}

#     response = requests.post(url=url, headers=headers, data=data)

#     access_token = response.json()["access_token"]
#     return access_token

# def get_auth_header(token):
#     return {"Authorization": "Bearer " + token}

# def get_artist_id(token, artist_name):
#     url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&market=BR&limit=1&offset=0"
#     headers = get_auth_header(token)
    
#     response = requests.get(url=url, headers=headers)
#     artist_id = response.json()["artists"]["items"]
#     return artist_id[0]["id"]

# def get_artist_top_tracks(token, artist_id):
#     url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=BR"
#     headers = get_auth_header(token)

#     response = requests.get(url=url, headers=headers)
#     artist_top_tracks = response.json()["tracks"]
#     return artist_top_tracks

# def get_user_top_artists(token):
#     url = "https://api.spotify.com/v1/me/top/artists?time_range=long_term&limit=50&offset=0"
#     headers = get_auth_header(token)

#     response = requests.get(url=url, headers=headers)
#     user_top_artists = response.json()
#     return user_top_artists
    
    
# auth_token = get_auth_token()
# artist_id = get_artist_id(auth_token, artist_name="blink182")
# artist_top_tracks = get_artist_top_tracks(auth_token, artist_id=artist_id)
# user_top_artists = get_user_top_artists(auth_token)

# print(user_top_artists)

# # for idx, song in enumerate(artist_top_tracks):
# #     print(f"{idx + 1}. {song['name']} {song['popularity']} {song['album']['name']}")