import pandas as pd
import re
import pathlib

def add_song(data: pd.DataFrame) -> None:
    track = input("Ingrese el título de la canción: ")
    artist = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del álbum: ")
    while True:
        album_type = input("Ingrese el tipo de álbum (album o single): ")
        if album_type != 'album' or album_type != 'single':
            print("Porfavor elegir solamente 'album' o 'single'.")
            continue
        else:
            break
    while True:
        url_spotify = input("Ingrese la URL de Spotify de la canción: ")
        if not re.match(r'^https:\/\/open\.spotify\.com\/[a-zA-Z0-9/?=_-]+$', url_spotify):
            print("URL de Spotify no válida.")
            continue
        else:
            break
    while True:
        uri = input("Ingrese el URI de Spotify de la canción: ")
        if not re.match(r'^spotify:track:[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$', uri):
            print("URI de Spotify no válida.")
            continue
        else:
            break
    while True:
        duration_ms = input("Ingrese la duración en segundos: ")
        if not re.match(r'^\d+$', duration_ms):
            print("Duración no válida.")
            continue
        else:
            break
    duration_ms = float(duration_ms) * 1000
    url_youtube = input("Ingrese la URL de YouTube: ")
    if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=&-]+)?$', url_youtube):
        print("URL de YouTube no válida.")
        return
    while True:
        while True:
            likes = input("Ingrese la cantidad de likes: ")
            if not re.match(r'^\d+$', likes):
                print("Likes no válidos.")
                continue
            else:
                break
        while True:
            views = input("Ingrese la cantidad de views: ")
            if not re.match(r'^\d+$', likes):
                print("Views no válidas.")
                continue
            else:
                break
        if likes > views:
            print("No puede haber más likes que views, vuelva a intentarlo.")
            continue
        else:
            break
    new_song = pd.DataFrame({
        "Index": [pd.read_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv").iloc[-1] + 1],
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
        "Licensed": ["False"],
        "official_video": ["False"],
        "Stream": ["0.0"],
    })

    # data = pd.concat([data, new_song], ignore_index=True)
    
    new_song.to_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv", mode='a', index=False)
    print("Canción agregada exitosamente.")