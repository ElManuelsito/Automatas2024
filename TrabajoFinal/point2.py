import pandas as pd
from tabulate import tabulate

def search_artist(data):
    search_term = input("Ingrese parte del nombre del artista: ")
    result = data[data["Artist"].str.contains(search_term, case=False, na=False)]
    
    table = tabulate(result[["Index", "Artist", "Title"]], headers="keys", tablefmt="pretty", showindex=False)
    
    print(table)