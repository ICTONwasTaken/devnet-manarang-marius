"""
Midterm Practical Exam — Movie Collection Manager
Student: Manarang, Marius L.
"""

movies = ["something - something - Watched"]


def display_menu():
    print("=== Movie Collection Manager ===")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Remove a movie")
    print("6. Exit")
    action = int(input("Choose an option: "))
    return action


def add_movie(movie_list:list):
    # ask for title, director, and status
    title = input("Movie title: ")
    director = input("Movie director: ")
    status = input("Movie status: ")
    print("")
    print(title, "successfully added!")
    print("")
    # build the movie string
    movie = f"{title} - {director} - {status}"
    # add it to the list
    movie_list.append(movie)
    return movie_list


def view_movies(movie_list):
    # loop through and print every movie
    print("=== All Movies ===")
    if movie_list:
        for movie in movie_list:
            print(movie)
    # handle empty list
    elif not movie_list:
            print("No movies here!")
    print("")


def count_watched_unwatched(movie_list):
    # loop through the list
    wa = []
    un = []
    w_count = 0
    u_count = 0

    for movie in movie_list:
        movie = movie.lower()

        if " watched" in movie:
            wa.append(movie)
        if " unwatched" in movie:
            un.append(movie)
    # count Watched vs Unwatched
    print("=== Watched Movies ===")
    for w in wa:
        w_count += 1
        print(w)
    print("")
    print("=== Unwatched Movies ===")
    for u in un:
            u_count += 1
            print(u)
    # return both counts
    return w_count, u_count


def find_movie(movie_list):
    found_list = []
    # ask for a movie title
    thingy = input("Search for Movie Title: ")
    print("")

    # search the list
    # search should be case-insensitive
    for movie in movie_list:
        found = movie.find(thingy)
        if found > -1:
            found_list.append(movie)
        else:
            continue
    # print the result or "Movie not found."
    if found_list:
        print("Movie found:")
        for movie in found_list:
            print(movie)
    else:
         print("Movie not found...")
    print("")

def remove_movie(movie_list):
    # ask for a movie title
    thingy = input("Movie Title to remove: ")
    print("")

    for movie in movie_list:
        found = movie.find(thingy)

        if found > -1:
            movie_list.remove(movie)

        if found >= 0:
            print("Movie successfully deleted")
        else:
            print("Movie not found...")

    return movie_list



def main():
    global movies
    action = 0
    loop = True
    # create the main menu loop

    while loop == True:
        action = display_menu()
        print("")
        # call the appropriate function based on the user's choice
        if action == 1:
            movies = add_movie(movies)
        if action == 2:
            view_movies(movies)
        if action == 3:
            w, u = count_watched_unwatched(movies)
            print("")
            print("Watched Movies: ", w)
            print("Unatched Movies: ", u)
            print("")
        if action == 4:
            find_movie(movies)
        if action == 5:
            movies = remove_movie(movies)
            print("")
        if action == 6:
            loop = False


main()