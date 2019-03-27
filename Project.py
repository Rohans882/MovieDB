
movies = []

def option():
    user_input = input("Enter 'add' to add a movie.\nEnter 'list' to see your movies.\nEnter 'find' to find a movie.\nEnter 'quit' to quit: ")
    if user_input != 'quit':
        if user_input == 'add':
            add_movie()
        elif user_input == 'list':
            show_movies(movies)
        elif user_input == 'find':
            find()
        else:
            print("Enter 'add' to add a movie.\nEnter 'list' to see your movies.\nEnter 'find' to find a movie.\nEnter 'quit' to quit: ")


def find():
    property_finder = input("Enter the property you wish to find the movie by: ")
    search = input("What are you searching: ")
    finder = property_finder_attribute(movies, search, lambda x: x[property_finder])
    if finder:
        show_movies(finder)
    else:
        print("No movies found...")

def property_finder_attribute(items, expected, finder):
    index = []
    for i in items:
        if finder(i) == expected:
            index.append(i)
    return index


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })

def show_movies(movies_list):
    for movie in movies_list:
        movie_details(movie)

def movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

option()