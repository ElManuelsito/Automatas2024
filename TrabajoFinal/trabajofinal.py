# LIBRERIAS QUE IMPORTAMOS (indicarlas y explicar por qué las usamos cuando hagamos la presentación)
import pathlib
import csv
import re
import time 
from dataclasses import dataclass


# CREACION DE DATACLASS PARA CANCIONES COMO HICIMOS CON MovieDto
# -------------------   -------------------
@dataclass
class SongDto:
    index: int
    artist: str
    url_spotify: str
    track: str
    album: str
    album_type: str
    uri: str
    danceability: float
    energy: float
    key: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration: float
    url_youtube: str
    youtube_video_title: str
    youtube_channel: str
    youtube_views: float
    youtube_likes: float
    comments:  float
    licensed: bool
    official_video: bool
    stream: float

    def func_de_ejemplo():
        pass
# -------------------   -------------------


# LECTURA DEL ARCHIVO PARA GUARDAR LOS REGISTROS EN UNA LISTA, CUIDADO AL MODIFICAR ESTO, NO AFECTA EL ARCHIVO PERO PUEDE HACER INUTIL EL CODIGO DE LOS EJERCICIOS MÁS ABAJO
# -------------------   -------------------
def parse_csv() -> list:
    songs = []
    try:
        with open(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv", 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                song = SongDto(
                    row['Index'],
                    row['Artist'],
                    row['Url_spotify'],
                    row['Track'],
                    row['Album'],
                    row['Album_type'],
                    row['Uri'],
                    row['Danceability'],
                    row['Energy'],
                    row['Key'],
                    row['Loudness'],
                    row['Speechiness'],
                    row['Acousticness'],
                    row['Instrumentalness'],
                    row['Liveness'],
                    row['Valence'],
                    row['Tempo'],
                    row['Duration_ms'],
                    row['Url_youtube'],
                    row['Title'],
                    row['Channel'],
                    row['Views'],
                    row['Likes'],
                    row['Comments'],
                    row['Licensed'],
                    row['official_video'],
                    row['Stream'],
                )
                songs.append(song)
        return songs
    except (FileNotFoundError):
        print('File not found')
        exit(1)
# -------------------   -------------------


# DEFINICIÓN DE FUNCIONES PARA CADA EJERCICIO DEL TRABAJO

# PUNTO 1 - Buscar por título o artista: se pedirá al usuario que ingrese texto representando
#           el título de la canción o artista que desee buscar. Tener en cuenta que la entrada
#           puede estar incompleta (por ejemplo, las primeras letras del título). También
#           considerar que la búsqueda debe ser independiente de si existen mayúsculas o
#           minúsculas (case insensitive). Ordenar por cantidad de reproducciones de manera
#           descendente. El resultado debe incluir solo el nombre del artista, el nombre de la
#           canción y la duración en formato HH:MM:SS.
# -------------------   -------------------
def punto_1():
    pass
# -------------------   -------------------



# PUNTO 2 - Dado un artista mostrar los 10 temas con mayor reproducciones, la información
#           que se debe mostrar en cada tema es: nombre del artista, nombre del tema,
#           duración (formato HH:MM:SS), cantidad de reproducciones (en millones).
# -------------------   -------------------
def punto_2():
    pass
# -------------------   -------------------



# PUNTO 3 - Insertar un registro, esto se debe poder realizar de dos maneras, desde un
#           archivo .csv, pudiendo insertar varios registros o de manera manual desde la
#           terminal. Los valores que se deben ingresar son: artista, track, album, Uri Spotify
#           (validar con ER), duración (se debe convertir a milisegundos), url de Spotify y url de
#           youtube, likes y views (no debería tener mas likes que views).
# -------------------   -------------------
def punto_3():
    pass
# -------------------   -------------------


# PUNTO 4 - Dado un artista mostrar la cantidad de álbumes que tiene y por cada álbum 
#           especificar el nombre, la cantidad de canciones, y la duración total del mismo.
# -------------------   -------------------
def show_artist_album_ammount_songs_per_album_ammount_and_album_duration(songs: list, artist: str) -> None:
    albums = {}
    for song in songs:
        if artist.lower() in song.artist.lower():
            artist = song.artist
            if song.album in albums:
                albums[song.album] = (albums[song.album][0] + 1, albums[song.album][1] + float(song.duration))
            else:
                albums[song.album] = (1, float(song.duration))
    print(f"{artist} tiene {len(albums.keys())} albums:")
    for album, amount_of_songs_and_duration in albums.items():
        print("\u2022", f"{album} tiene {amount_of_songs_and_duration[0]} canciones y dura {time.strftime('%H:%M:%S', time.gmtime(amount_of_songs_and_duration[1]/1000))}")

# -------------------   -------------------


# OTRAS FUNCIONES PARA SIMPLIFICAR LA EJECUCION PRINCIPAL o SIMPLIFICAR OTRAS FUNCIONES (si es q hace falta)
# -------------------   -------------------
def otra_func_de_ejemplo1():
    pass

def otra_func_de_ejemplo2():
    pass

def show_multiple_songs(songs: list) -> None:
    #  esta funcion la hice para testear que ande el SongDto y la lista q returna, borrarlo o reusarlo desp como mejor venga
    print(f'\nCanciones:')
    for song in songs[:25]:
        print("\u2022", f'{song.artist} - {song.track} (loudness: {song.loudness}) (is official: {song.official_video})')
    return
# -------------------   -------------------


# EJECUCIÓN DE MENU Y LLAMADAS (EJECUCIÓN PRINCIPAL)
if __name__ == '__main__':
    songs = parse_csv()
    show_artist_album_ammount_songs_per_album_ammount_and_album_duration(songs, input("Ingrese artista: "))
    # show_multiple_songs(songs)
    # albums = {'Demon Days' : (1, 34922), 'Plastic Beach' : (3, 78333)}
    # albums['Demon Days'] = (2, albums['Demon Days'][1])
    # print(albums['Demon Days'][0])
    # albums = [('Demon Days', 1, 34922), ('Plastic Beach', 3, 78333)]
    # print(albums[albums.index('Demon Days')][1])
