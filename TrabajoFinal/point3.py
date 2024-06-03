import pandas as pd
import re

def add_song(data: pd.DataFrame) -> None:
    title = input("Ingrese el título de la canción: ")
    artist = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del álbum: ")
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
        "Title": [title],
        "Artist": [artist],
        "Album": [album],
        "Url_spotify": [url_spotify],
        "Uri": [uri],
        "Duration_ms": [int(duration_ms)],
        "Url_youtube": [url_youtube],
        "Likes": [likes],
        "Views": [views],
    })

    data = pd.concat([data, new_song], ignore_index=True)
    
    data.to_csv("spotify_and_youtube_2024.csv", index=False)
    print("Canción agregada exitosamente.")