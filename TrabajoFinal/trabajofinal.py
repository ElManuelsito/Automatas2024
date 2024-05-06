import pathlib
import csv
import re
from dataclasses import dataclass

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

    def foo_bar():
        pass


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
        print("File not found")
        exit(1)

def show_multiple_songs(songs: list) -> None:
    print(f'\nCanciones:')
    for song in songs[:25]:
        print("\u2022", f'{song.artist} - {song.track} (loudness: {song.loudness}) (is official: {song.official_video})')
    return

if __name__ == '__main__':
    songs = parse_csv()
    show_multiple_songs(songs)