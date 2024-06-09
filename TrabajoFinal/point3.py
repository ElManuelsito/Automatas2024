import pandas as pd
import re
import pathlib

def add_song(data: pd.DataFrame) -> None:
    track = input("Ingrese el título de la canción: ")
    artist = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del álbum: ")
    album_type = input("Ingrese el tipo de álbum (álbum o single): ")
    url_spotify = input("Ingrese la URL de Spotify de la canción: ")
    uri = input("Ingrese el URI de Spotify de la canción: ")
    duration_ms = input("Ingrese la duración en milisegundos: ")
    url_youtube = input("Ingrese la URL de YouTube: ")
    likes = input("Ingrese la cantidad de likes: ")
    views = input("Ingrese la cantidad de views: ")

    if not re.match(r'^https:\/\/open\.spotify\.com\/[a-zA-Z0-9/?=_-]+$', url_spotify):
        print("URL de Spotify no válida.")
        return
        
    if not re.match(r'^spotify:track:[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$', uri):
        print("URI de Spotify no válida.")
        return

    if not re.match(r'^\d+$', duration_ms):
        print("Duración no válida.")
        return

    if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=&-]+)?$', url_youtube):
        print("URL de YouTube no válida.")
        return

    new_song = pd.DataFrame({
        "Artist": [artist],
        "Url_spotify": [url_spotify],
        "Track": [track],
        "Album": [album],
        "Album_type": [album_type],
        "Uri": [uri],
        "Energy": ["0.0"],
        "Key": ["0.0"],
        "Loudness": ["0.0"],
        "Speechiness": ["0.0"],
        "Acousticness": ["0.0"],
        "Instrumentalness": ["0.0"],
        "Liveness": ["0.0"],
        "Valence": ["0.0"],
        "Tempo": ["0.0"],
        "Duration_ms": [duration_ms],
        "Url_youtube": [url_youtube],
        "Title": [""],
        "Channel": [""],
        "Views": [views],
        "Likes": [likes],
        "Comments": ["0.0"],
        "Licensed": ["None"],
        "official_video": ["None"],
        "Stream": ["0.0"],
    })

    data = pd.concat([data, new_song], ignore_index=True)
    
    data.to_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube_2024.csv", index=False)
    print("Canción agregada exitosamente.")