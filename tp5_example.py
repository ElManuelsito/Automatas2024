import pathlib
import csv
from dataclasses import dataclass

# Creamos clase DTO que representa una fila.
# Ver https://realpython.com/python-data-classes
@dataclass
class MovieDto:
    title: str
    year: str
    age: str
    rating: float
    available_in_netflix: bool
    available_in_hulu: bool
    available_in_prime_video: bool
    available_in_disney_plus: bool

    def rating_as_float(self) -> float:
        score = int(self.rating.split('/')[0])
        return score / 100

def parse_csv() -> list:
    movies = []
    try:
        # Abrir el archivo csv usando path relativo desde este archivo Python
        with open(f"{pathlib.Path(__file__).parent.absolute()}/movies.csv", 'r', encoding='utf-8') as file:
            # Usamos csv.DictReader que permite leer el archivo y parsear cada fila a un diccionario Python.
            # ver https://realpython.com/python-csv/
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
            # Parseamos cada row a la clase DTO. Lo agregamos a la lista
                movie = MovieDto(
                    row['Title'],
                    row['Year'],
                    row['Age'],
                    row['Rating'],
                    row['Netflix'] == '1',
                    row['Hulu'] == '1',
                    row['Prime Video'] == '1',
                    row['Disney+'] == '1',
                )
                movies.append(movie)
        return movies
    except (FileNotFoundError):
        print("File not found")
        exit(1)

# while True:
#     print("1. Add movie")
#     print("2. Search movie")
#     print("3. Exit")
#     choice = input("Choose an option: ")
#     if choice == '1':
#         movie_details = get_movie_details_from_user()
#         add_movie_to_csv(movie_details)
#     elif choice == '2':
#         user_search_text = input("Ingrese el texto de búsqueda (puede ser incompleto): ")
#         search_movie_by_title(user_search_text)
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice. Please choose again.")

def get_movie_details_from_user() -> MovieDto:
    title = input("Ingrese el título de la película: ")
    year = input("Ingrese el año de la película: ")
    age = input("Ingrese la clasificación por edad (por ejemplo, PG-13): ")
    rating = input("Ingrese la calificación (por ejemplo, 7.5/10): ")
    # Pregunta sobre disponibilidad en servicios de transmisión
    # ...

    # Validar la calificación como un número decimal
    try:
        rating_as_float = float(rating.split('/')[0])
        if not (0 <= rating_as_float <= 10):
            raise ValueError("La calificación debe estar entre 0 y 10.")
    except ValueError:
        print("Error: La calificación no es válida.")
        exit(1)

    return MovieDto(title, year, age, rating, False, False, False, False)

def add_movie_to_csv(movie: MovieDto):
    try:
        with open(f"{pathlib.Path(__file__).parent.absolute()}/movies.csv", 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([movie.title, movie.year, movie.age, movie.rating, 0, 0, 0, 0])  # Las columnas de disponibilidad se inicializan en 0
        print("Película agregada correctamente al archivo.")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        exit(1)

def search_movie_by_title(search_text):
    try:
        # Abrir el archivo csv usando path relativo desde este archivo Python
        with open(f"{pathlib.Path(__file__).parent.absolute()}/movies.csv", 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                # Convertir el título de la película y el texto de búsqueda a minúsculas
                if search_text.lower() in row['Title'].lower():
                    print(f"Se encontró la película: {row['Title']}")
                    return
            print("No se encontraron películas con ese título.")
    except FileNotFoundError:
        print("Archivo no encontrado")
        exit(1)

while True:
    print("1. Buscar película por título")
    print("2. Agregar película al archivo CSV")
    print("3. Salir")
    option = input("Elija una opción: ")

    if option == "1":
        search_text = input("Ingrese el texto de búsqueda: ")
        search_movie_by_title(search_text)
    elif option == "2":
        get_movie_details_from_user()
    elif option == "3":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

# if __name__ == '__main__':
#     new_movie = get_movie_details_from_user()
#     add_movie_to_csv(new_movie)


# if __name__ == '__main__':
#     # Obtenemos lista de películas como una lista de DTOs
#     movies = parse_csv()
#     # Mostramos el primer DTO y algunos de sus atributos
#     print(movies[0])
#     print(movies[0].title)
#     print(movies[0].year)
#     print(movies[0].available_in_netflix)
#     print(movies[0].rating_as_float())