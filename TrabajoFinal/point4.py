
def top_artists(songs: list, artist: str) -> None:
    albums = {}
    for song in songs:
        if artist.lower() in song.artist.lower():
            artist = song.artist
            if song.album in albums:
                albums[song.album] = (albums[song.album][0] + 1, albums[song.album][1] + float(song.duration))
            else:
                albums[song.album] = (1, float(song.duration))
    print(f"{artist} tiene {len(albums.keys())} albums:")
    for album, songs_duration in albums.items():
        print("\u2022", f"{album} tiene {songs_duration[0]} canciones y dura {time.strftime('%H:%M:%S', time.gmtime(songs_duration[1]/1000))}")