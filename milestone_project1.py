movies = [
    {"name": "The Evil Dead", "director": "Sam Raimi", "year": '1981'},
    {"name": "RoboCop", "director": "Paul Verhoeven", "year": '1987'},
    {"name": "Beauty and the Beast", "director": "Jean Cocteau", "year": '1946'},
    {"name": "Nosferatu", "director": "F.W. Murnau", "year": '1922'}
]


print("Welcome to the Film Storage Project, please make a selection: ")

def menu():
    choice = input("\n1: View all selected movies\n2: Add to movie collection"
                   "\n3: Find film by attribute\n4:To quit the application\n\n: ")

    while choice != "4":
        if choice == "1":
            show_movies(movies)
        elif choice == "2":
            add_movie()
        elif choice == "3":
            find_movie()
        else:
            print("Invalid entry. Please enter a number from 1 -4 for a valid choice.")

        choice = input("\n1: View all selected movies\n2: Add to movie collection\n3: Find film by attribute\n4: To quit the application\n\n: ")


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}\n"
          f"Director: {movie['director']}\n"
          f"Released: {movie['year']}\n")

def add_movie():
    new_name = (input("To add a new film, let's begin with the name of the film: "))
    new_director = input("Who is the director of this film?: ")
    new_year = (input("Which year was this film released?: "))

    movies.append({
        "name": new_name,
        "director": new_director,
        "year": new_year
    })

def find_movie():
    find_by = input("What property of the movie are you looking for?: ")
    looking_for = input("What are you searching for?: ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)

def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
        else:
            "Invalid entry"

    return found


menu()
