import pandas as pd
from tabulate import tabulate

def search_song_or_artist(data: pd.DataFrame) -> None:
    while True:
        user_search_input = input("Ingrese el título o artista: ")
        if len(user_search_input) < 3 or user_search_input == '':
            print("Por favor ingresa al menos 3 caracteres")
            continue
        break
    data["Duration_min"] = data["Duration_ms"].apply(lambda x: '{:02}:{:02}'.format(x // 60000, (x // 1000) % 60))
    result = data[data["Title"].str.contains(user_search_input, case=False, na=False)]    
    result = result.sort_values(by="Views", ascending=False)
    
    result_table = tabulate(result[["Views", "Title", "Artist", "Duration_min"]], headers="keys", tablefmt="pretty", showindex=False)
    print(result_table)