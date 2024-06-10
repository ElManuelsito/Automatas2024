import pandas as pd, os, time, pathlib
from point1 import search_song_or_artist
from point2 import show_top_10_tracks_from_artist
from point3 import add_song_from_input, add_song_from_file
from point4 import show_artist_album_info


GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

os.system('cls')
print(f"{BLUE}Reading File...")
data = pd.read_csv(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv")

while True:
    print(f"{BLUE}")
    print("Menu:")
    print("1. Buscar por título o artista")
    print("2. Buscar 10 mejores canciones de un artista")
    print("3. Añadir nueva canción al archivo")
    print("4. Buscar álbumes de un artista")
    print("5. Salir")
    print(f"{RESET}")

    option = input("Opción: ")

    if option == "1":
        print(f"{GREEN}")
        search_song_or_artist(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "2":
        print(f"{GREEN}")
        show_top_10_tracks_from_artist(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "3":
        print(f"{GREEN}")
        print("Elija cómo ingresar una nueva canción:\n1. Por consola\n2. Con un archivo")
        append_type_option = input("Opción: ")
        if append_type_option == "1":
            add_song_from_input()
        elif append_type_option == "2":
            add_song_from_file(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "4":
        print(f"{GREEN}")
        show_artist_album_info(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "5":
        break
    else:
        print("Opción inválida. Intenta otra vez.")
        time.sleep(1.3)