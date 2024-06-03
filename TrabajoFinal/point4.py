
# def top_artists(Title: list, artist: str) -> None:
#     albums = {}
#     for song in Title:
#         if artist.lower() in song.artist.lower():
#             artist = song.artist
#             if song.album in albums:
#                 albums[song.album] = (albums[song.album][0] + 1, albums[song.album][1] + float(song.Duration_ms))
#             else:
#                 albums[song.album] = (1, float(song.Duration_ms))
#     print(f"{artist} have {len(albums.keys())} albums:")
#     for album, Title_Duration_ms in albums.items():
#         print("\u2022", f"{album} have {Title_Duration_ms[0]} Title & time {time.strftime('%H:%M:%S', time.gmtime(Title_Duration_ms[1]/1000))}")

# import pandas as pd

# def top_artists(data: pd.DataFrame) -> None:
#     data['Views'] = pd.to_numeric(data['Views'], errors='coerce')
#     artist_views = data.groupby('Artist')['Views'].sum().sort_values(ascending=False).head(10)
    
#     print("Top 10 artists with most views:")
#     for i, (artist, views) in enumerate(artist_views.items(), start=1):
#         print(f"{i}. {artist}: {views} views")
# import pandas as pd

# def top_artists(data: pd.DataFrame) -> None:
#     data['Views'] = pd.to_numeric(data['Views'], errors='coerce')
    
#     nombre_artista = input("Ingresa el nombre del artista: ")
    
#     # artist_data = data[data['Artist'].str.lower() == nombre_artista.lower()]
#     artist_data = data[data["Artist"].str.contains(nombre_artista, case=False, na=False)]

#     if artist_data.empty:
#         print(f"No se encontraron álbumes para el artista '{nombre_artista}'.")
#     else:
#         print(f"Álbumes para el artista '{nombre_artista}':")
#         for i, row in artist_data.iterrows():
#             print(f"Álbum: {row['Album']}")
#             songs_per_album = artist_data.groupby(["Album", "Title"])
#             print(f"   - Canciones: {len(songs_per_album)}")
#             print(f"   - Duración total: {row['Duration_ms']} segundos\n")
import pandas as pd
import time

def top_artists(data: pd.DataFrame) -> None:
    data['Views'] = pd.to_numeric(data['Views'], errors='coerce')
    
    nombre_artista = input("Ingresa el nombre del artista: ")
    
    artist_data = data[data["Artist"].str.contains(nombre_artista, case=False, na=False)]

    if artist_data.empty:
        print(f"No se encontraron álbumes para el artista '{nombre_artista}'.")
    else:
        print(f"Álbumes para el artista '{nombre_artista}':")
        albums_grouped = artist_data.groupby("Album")
        for album, album_group in albums_grouped:
            print(f"Álbum: {album}")
            num_songs = len(album_group)
            print(f"   - Canciones: {num_songs}")
            total_duration = album_group['Duration_ms'].sum() // 1000  # Duración total en segundos
            print(f"   - Duración total: {time.strftime('%H:%M:%S', time.gmtime(total_duration))}")