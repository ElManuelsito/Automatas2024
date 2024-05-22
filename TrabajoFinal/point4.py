
# def top_artists(songs: list, artist: str) -> None:
#     albums = {}
#     for song in songs:
#         if artist.lower() in song.artist.lower():
#             artist = song.artist
#             if song.album in albums:
#                 albums[song.album] = (albums[song.album][0] + 1, albums[song.album][1] + float(song.duration))
#             else:
#                 albums[song.album] = (1, float(song.duration))
#     print(f"{artist} have {len(albums.keys())} albums:")
#     for album, songs_duration in albums.items():
#         print("\u2022", f"{album} have {songs_duration[0]} songs & time {time.strftime('%H:%M:%S', time.gmtime(songs_duration[1]/1000))}")

import pandas as pd

def top_artists(data: pd.DataFrame) -> None:
    data['Views'] = pd.to_numeric(data['Views'], errors='coerce')
    artist_views = data.groupby('Artist')['Views'].sum().sort_values(ascending=False).head(10)
    
    print("Top 10 artists with most views:")
    for i, (artist, views) in enumerate(artist_views.items(), start=1):
        print(f"{i}. {artist}: {views} views")
