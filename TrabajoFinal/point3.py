from tabulate import tabulate
import pandas as pd

def search_song(data):
    search_theme = input("Enter title of the song: ")
    
    # Convertir la duración de milisegundos a HH:MM:SS
    data["Duration_min"] = data["Duration_ms"].apply(lambda x: '{:02}:{:02}'.format(x // 60000, (x // 1000) % 60))
    
    # Filtrar canciones según el título buscado
    result = data[data["Title"].str.contains(search_theme, case=False, na=False)]
    
    # Ordenar las canciones por número de vistas
    result = result.sort_values(by="Views", ascending=False)

    # Crear la tabla de resultados
    result_table = tabulate(result[["Views", "Title", "Artist", "Duration_min"]], headers="keys", tablefmt="pretty", showindex=False)
    print(result_table)