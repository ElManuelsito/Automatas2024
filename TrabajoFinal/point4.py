import pandas as pd
import time

def show_artist_album_info(data: pd.DataFrame) -> None:
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