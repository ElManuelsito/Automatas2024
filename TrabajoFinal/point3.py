import pandas as pd
import re
import pathlib
import os

def add_song_from_input() -> None:
    track = input("Ingrese el título de la canción: ")
    artist = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del álbum: ")
    while True:
        album_type = input("Ingrese el tipo de álbum (album/single): ")
        if album_type != 'album' and album_type != 'single':
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
            if not re.match(r'^\d+$', views):
                print("Views no válidas.")
                continue
            else:
                break
        if int(likes) > int(views):
            print("No puede haber más likes que views, vuelva a intentarlo.")
            continue
        else:
            break
    new_song = pd.DataFrame({
        "Index": [str(int(pd.read_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv").iloc[-1]['Index']) + 1)],
        "Artist": [artist],
        "Url_spotify": [url_spotify],
        "Track": [track],
        "Album": [album],
        "Album_type": [album_type],
        "Uri": [uri],
        "Danceability": ["0.0"],
        "Energy": ["0.0"],
        "Key": ["0.0"],
        "Loudness": ["0.0"],
        "Speechiness": ["0.0"],
        "Acousticness": ["0.0"],
        "Instrumentalness": ["0.0"],
        "Liveness": ["0.0"],
        "Valence": ["0.0"],
        "Tempo": ["0.0"],
        "Duration_ms": [str(duration_ms)],
        "Url_youtube": [url_youtube],
        "Title": [""],
        "Channel": [""],
        "Views": [str(views)],
        "Likes": [str(likes)],
        "Comments": ["0.0"],
        "Licensed": ["False"],
        "official_video": ["False"],
        "Stream": ["0.0"],
    })
    new_song.to_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv", mode='a', index=False, header=False)
    print("Canción agregada exitosamente.")

# https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ
# spotify:track:0d28khcov6AiegSCpG5TuT
# https://www.youtube.com/watch?v=HyHNuVaZJ-k

def add_song_from_file(data: pd.DataFrame) -> None:
    while True:
        file = input("Ingrese el nombre del archivo (por ejemplo, canciones.csv): ")
        if not os.path.isfile(f"{pathlib.Path(__file__).parent.absolute()}/{file}"):
            path = input("No se ha encontrado ese archivo en la ruta actual\nIngrese la ruta de su archivo (por ejemplo, 'C:/Users/Juan/Downloads/'): ")
            if not os.path.isfile(f"{path}{file}"):
                if not os.path.isfile(f"{path}/{file}"):
                    print("No se ha encontrado ese archivo o la ruta es incorrecta, vuelva a intentarlo.")
                    continue
                file = pd.read_csv(f"{path}/{file}")
                break
            file = pd.read_csv(f"{path}{file}")
            break
        file = pd.read_csv(f"{pathlib.Path(__file__).parent.absolute()}/{file}")
        break
    if not 'Index' in file.columns:
        file.insert(0,"Index", None, False)
    filtered_file = pd.DataFrame(columns=file.columns)
    prev_index = int(data['Index'].iloc[-1])
    valid_values_present = False
    for i, row in file.iterrows():
        if 'Album_type' in file.columns:
            if str(file.loc[i, 'Album_type']) != 'album' and str(file.loc[i, 'Album_type']) != 'single':
                continue
        if 'Url_spotify' in file.columns:
            if not re.match(r'^https:\/\/open\.spotify\.com\/[a-zA-Z0-9/?=_-]+$', str(file.loc[i, 'Url_spotify'])):
                continue
        if 'Uri' in file.columns:
            if not re.match(r'^spotify:track:[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$', str(file.loc[i, 'Uri'])):
                continue
        if 'Duration_ms' in file.columns:
            if not re.match(r"^\d+$", str(file.loc[i, 'Duration_ms'])):
                continue
        if 'Url_youtube' in file.columns:
            if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=&-]+)?$', str(file.loc[i, 'Url_youtube'])):
                continue
        if 'Likes' in file.columns:
            if not re.match(r'^\d+$', str(file.loc[i, 'Likes'])):
                continue
        if 'Views' in file.columns:
            if not re.match(r'^\d+$', str(file.loc[i, 'Views'])):
                continue
        if 'Likes' in file.columns and 'Views' in file.columns:
            if int(file.loc[i, 'Likes']) > int(file.loc[i, 'Views']):
                continue
        if i == 0:
            file.at[0, 'Index'] = prev_index + 1
            valid_values_present = True
            current_index = prev_index + 1
        elif file.loc[i, 'Index'] == None and file.loc[i - 1, 'Index'] == None and not valid_values_present:
            file.at[i, 'Index'] = prev_index + 1
            valid_values_present = True
            current_index = prev_index + 1
        elif file.loc[i, 'Index'] == None and file.loc[i - 1, 'Index'] == None and valid_values_present:
            file.at[i, 'Index'] = current_index + 1
        else:
            file.at[i, 'Index'] = file.loc[i - 1, 'Index'] + 1
            current_index = file.loc[i - 1, 'Index'] + 1
        filtered_file = pd.concat([filtered_file, file.iloc[[i]]])
    filtered_file.reset_index(inplace=True, drop=True)
    for i, column_to_add in enumerate(data.columns.tolist()):
        try:
            if not column_to_add == filtered_file.columns[i]:
                filtered_file.insert(i, column_to_add, None, False)
        except IndexError:
            filtered_file[column_to_add] = None
    filtered_file = filtered_file.fillna({'Artist': '',
                                         'Track': '',
                                         'Album': '',
                                         'Danceability': '0.0',
                                         'Energy': '0.0',
                                         'Key': '0.0',
                                         'Loudness': '0.0',
                                         'Speechiness': '0.0',
                                         'Acousticness': '0.0',
                                         'Instrumentalness': '0.0',
                                         'Liveness': '0.0',
                                         'Valence': '0.0',
                                         'Tempo': '0.0',
                                         'Title': '',
                                         'Channel': '',
                                         'Comments': '0.0',
                                         'Licensed': 'False',
                                         'official_video': 'False',
                                         'Stream': '0.0'})
    filtered_file.to_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv", mode='a', index=False, header=False)
    print("Proceso finalizado correctamente. Note que es posible que no se hayan agregado algunas canciones debido a su formato incompleto o inválido.")