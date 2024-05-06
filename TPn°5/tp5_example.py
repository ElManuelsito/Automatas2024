import pathlib
import csv
import re
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
        score = self.rating.split('/')[0]
        if score.isdigit():
            score = int(score)
            return score / 100
        else:
            score = float(score)
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

def show_multiple_movies(movies: list, year: str = "cualquiera", age: str = "cualquiera", rating: str = "cualquiera", platform: str = "cualquiera") -> None:
    # muestra todas las peliculas de una lista pasada como argumento y las preferencias de busqueda que se mostrarán por pantalla (tmb como argumentos)
    print(f"\nPeliculas disponibles para filtros:\nAño: {year}\nEdad: {age}\nNota: {rating}\nPlataforma: {platform}\n")
    if rating != "cualquiera":
        for movie in movies:
            print("\u2022", movie.title, movie.rating)
    return

def search_movie_by_title(movies: list, search_text: str) -> None:
    # busca una pelicula por titulo a base de una cadena ingresada por el usuario como argumento. case insensitive.
    for movie in movies:
        # convertimos el título de la película y el texto de búsqueda a minúsculas
        if search_text.lower() in movie.title.lower():
            print(f"\nSe encontró la película: {movie.title}")
            return

def movie_from_details_by_user() -> MovieDto:
    # solicita al usuario ingresar los datos de una nueva peli a agregar, verifica que los datos sean válidos y devuelve un MovieDto
    user_set_for_yes = {"si","sí","sI","sÍ","Si","Sí","SI","SÍ"}
    title = input("Ingrese el título de la película: ")
    year = input("Ingrese el año de la película: ")
    while True:
        if not re.fullmatch(r"^([0-9]*\.?[0-9]+|[0-9]+\.?[0-9]*)$", year):
            year = input("Año invalido, por favor ingresa un año valido (1888-2024): ")
            continue
        if not 1888 <= int(year) <= 2024:
            year = input("Año invalido, por favor ingresa un año valido (1888-2024): ")
            continue
        break
    age = input("Ingrese la clasificación por edad (opciones: 7+, 13+, 16+ y 18+): ")
    while True:
        if not re.fullmatch(r"(7\+|13\+|16\+|18\+)", age):
            if not re.fullmatch(r"(7|13|16|18)", age):
                age = input("Edad invalida, por favor ingresa solo una edad valida (7+, 13+, 16+ o 18+): ")
                continue
            age = age + "+"
        break
    rating = input("Ingrese la calificación (por ejemplo, 7.5 o 54. Números como 7.654 serán redondeados a un decimal): ")
    while True:
        if not re.fullmatch(r"^([0-9]*\.?[0-9]+|[0-9]+\.?[0-9]*)$", rating):
            rating = input("Nota invalida, por favor ingresar una nota válida (0-100): ")
            continue
        rating = round(float(rating), 1)
        if rating.is_integer():
            rating = int(rating)
        if not 0 <= rating <= 100:
            rating = input("Nota invalida, por favor ingresar una nota válida (0-100): ")
            continue
        rating = str(rating) + "/100"
        break    
    print("Respona \"si\" o \"no\" a las plataformas en la que la película estará disponible")
    if input("Netflix: ") in user_set_for_yes:
        netflix = 1
    else:
        netflix = 0
    if input("Hulu: ") in user_set_for_yes:
        hulu = 1
    else:
        hulu = 0
    if input("Prime Video: ") in user_set_for_yes:
        prime_video = 1
    else:
        prime_video = 0
    if input("Disney+: ") in user_set_for_yes:
        disney_plus = 1
    else:
        disney_plus = 0
    return MovieDto(title, year, age, rating, netflix, hulu, prime_video, disney_plus)

def add_movie_to_csv(movie: MovieDto) -> None:
    # añade una nueva fila al archivo csv a base de un MovieDto como argumento
    try:
        with open(f"{pathlib.Path(__file__).parent.absolute()}/movies.csv", 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([movie.title, movie.year, movie.age, movie.rating, movie.available_in_netflix, movie.available_in_hulu, movie.available_in_prime_video, movie.available_in_disney_plus])
        print("Película agregada correctamente al archivo.")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        exit(1)

def movies_by_platform_and_age(movies: list, platform_selected: str, age_selected: str) -> list:
    # chequea si las pelis en una lista dada como argumento están en la plataforma que eligió el usuario, y las filtra con 'filter_movie_by_age' para devolver una lista con solamente pelis que cumplan con ambos criterios
    filtered_movies = []
    if not movies:
        print("No hay peliculas a filtrar por plataforma y edad")
        return movies
    if platform_selected == "Netflix":
        for movie in movies:
            if movie.available_in_netflix == True:
                if filter_movie_by_age(age_selected, movie):
                    filtered_movies.append(movie)
    elif platform_selected == "Hulu":
        for movie in movies:
            if movie.available_in_hulu == True:
                if filter_movie_by_age(age_selected, movie):
                    filtered_movies.append(movie)
    elif platform_selected == "Prime Video":
        for movie in movies:
            if movie.available_in_prime_video == True:
                if filter_movie_by_age(age_selected, movie):
                    filtered_movies.append(movie)
    elif platform_selected == "Disney+":
        for movie in movies:
            if movie.available_in_disney_plus == True:
                if filter_movie_by_age(age_selected, movie):
                    filtered_movies.append(movie)
    return filtered_movies

def filter_movie_by_age(age_selected: str, movie: MovieDto) -> bool:
    # filtra una pelicula dada comparando su edad con la edad que eligió el usuario, si coinciden, devuelve True para ser añadida a la lista de cualquier otra funcion que requiera filrar por edad. De no coincidir, simplemente False.
    # edades disponibles por ahora: 7+, 13+, 16+, 18+
    if age_selected == "7+" and movie.age == "7+":
        return True
    elif age_selected == "13+" and movie.age == "13+":
        return True
    elif age_selected == "16+" and movie.age == "16+":
        return True
    elif age_selected == "18+" and movie.age == "18+":
        return True
    else:
        return False

def movies_by_highest_rank(movies: list, limit: int = 10) -> list:
    # compara los rankings usando rating_as_float y devuelve una lista con las pelis de mejor a peor nota
    # la peli con la mejor nota está al principio, y cada vez que aparezca una peli con menor nota que la anterior se añade debajo 
    # (si aparece una menor a otra pero tambien mayor a otra se queda entre medio de esas, si aparece una de igual ranking se pone abajo de la primera peli con igual nota encontrada)
    if not movies:
        print("No hay películas a filtrar por nota")
        return movies
    ranked_movies = [movies[0]]
    for movie in movies[1:]:
        if movie.rating_as_float() > ranked_movies[0].rating_as_float():
            ranked_movies.insert(0, movie)
        elif movie.rating_as_float() == ranked_movies[0].rating_as_float():
            ranked_movies.insert(1, movie)
        elif movie.rating_as_float() < ranked_movies[0].rating_as_float():
            if len(ranked_movies) > 1:
                for ranked_movie in ranked_movies[1:]:
                    if movie.rating_as_float() < ranked_movie.rating_as_float():
                        if ranked_movies.index(ranked_movie) + 1 == len(ranked_movies):
                            ranked_movies.append(movie)
                            break
                        elif ranked_movies.index(ranked_movie) + 1 == limit:
                            break
                        else:
                            continue
                    elif movie.rating_as_float() == ranked_movie.rating_as_float():
                        ranked_movies.insert(ranked_movies.index(ranked_movie) + 1, movie)
                        break
                    elif movie.rating_as_float() > ranked_movie.rating_as_float():
                        ranked_movies.insert(ranked_movies.index(ranked_movie), movie)
                        break
            else:
                ranked_movies.append(movie)
    ranked_movies_limited = ranked_movies[:limit]
    return ranked_movies_limited

def get_user_platform_choice(option: str) -> str:
    while True:
        if option == "1":
            option = "Netflix"
            return option
        elif option == "2":
            option = "Hulu"
            return option
        elif option == "3":
            option = "Prime Video"
            return option
        elif option == "4":
            option = "Disney+"
            return option
        else:
            option = input("Opción inválida, por favor ingresar una opción válida (1, 2, 3, etc): ")

def get_user_age_choice(option: str) -> str:
    while True:
        if option == "1":
            option = "7+"
            return option
        elif option == "2":
            option = "13+"
            return option
        elif option == "3":
            option = "16+"
            return option
        elif option == "4":
            option = "18+"
            return option
        else:
            option = input("Opción inválida, por favor ingresar una opción válida (1, 2, 3, etc): ")

def get_user_rating_choice(option: str) -> str:
    while True:
        if option == "1":
            option = "mejor a peor"
            return option
        else:
            option = input("Opción inválida, por favor ingresar una opción válida (1, 2, 3, etc): ")

if __name__ == '__main__':
    while True:
        # Obtenemos lista de películas como una lista de DTOs
        movies = parse_csv()
        print("\n1. Buscar película por título\n2. Mostrar películas por plataforma y edad\n3. Agregar película al archivo CSV\n4. Salir")
        option = input("Elija una opción: ")
        if option == "1":
            search_movie_by_title(movies, input("Ingrese el texto de búsqueda: "))
        elif option == "2":
            print("\nSeleccionar plataforma:\n1. Netflix\n2. Hulu\n3. Prime Video\n4. Disney+\n")
            user_platform_choice = get_user_platform_choice(input("Opción: "))
            print("\nSeleccionar edad:\n1. 7+\n2. 13+\n3. 16+\n4. 18+\n")
            user_age_choice = get_user_age_choice(input("Opción: "))
            print("\nSeleccionar nota:\n1. Mejor a peor\n")
            user_rating_choice = get_user_rating_choice(input("Opción: "))
            show_multiple_movies(movies_by_highest_rank(movies_by_platform_and_age(movies, user_platform_choice, user_age_choice)), age = user_age_choice, rating = user_rating_choice, platform = user_platform_choice)
        elif option == "3":
            add_movie_to_csv(movie_from_details_by_user())
        elif option == "4":
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
