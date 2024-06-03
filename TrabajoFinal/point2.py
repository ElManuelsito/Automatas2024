import pandas as pd
from tabulate import tabulate

def show_top_10_tracks_from_artist(data: pd.DataFrame) -> None:
    search_artist = input("Ingresa el nombre del artista: ")
    result = data[data["Artist"].str.contains(search_artist, case=False, na=False)].copy()
    result = result.sort_values(by="Views", ascending=False)
    top_10 = result.head(10)
    top_10.loc[:, "Duration"] = top_10["Duration_ms"].apply(lambda x: '{:02}:{:02}:{:02}'.format(x // 3600000, (x // 60000) % 60, (x // 1000) % 60))
    top_10.loc[:, "Views (millions)"] = top_10["Views"] / 1_000_000

    result_table = top_10[["Artist", "Title", "Duration", "Views (millions)"]]
    print(tabulate(result_table, headers="keys", tablefmt="pretty", showindex=False))