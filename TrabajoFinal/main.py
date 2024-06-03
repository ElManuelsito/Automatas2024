import pandas as pd, os, time, pathlib
from point1 import search_song_or_artist
from point2 import top_10_from_artist
from point3 import add_song
from point4 import artist_album_info

# Ruta Augusto
# data = pd.read_csv("C:/Users/acast/OneDrive/Documents/UM/2024/Automátas y Gramáticas/Automatas nuevo/Automatas2024/TrabajoFinal/spotify_and_youtube 2024.csv")

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
        top_10_from_artist(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "3":
        print(f"{GREEN}")
        add_song(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "4":
        print(f"{GREEN}")
        artist_album_info(data)
        print(f"{RESET}")
        # time.sleep(3)
    elif option == "5":
        break
    else:
        print("Opción inválida. Intenta otra vez.")
        time.sleep(2)