"""
Midterm Practical Exam — Movie Collection Manager
Student: [your name]
"""

movies = []


def display_menu():
    print("=== Movie Collection Manager ===")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    action = int(input("Choose an option: "))
    return action


def add_movie(movie_list:list):
    # ask for title, director, and status
    title = input("Movie title: ")
    director = input("Movie director: ")
    status = input("Movie status: ")
    # build the movie string
    movie = f"{title} - {director} - {status}"
    # add it to the list
    movie_list.append(movie)
    return movie_list


def view_movies(movie_list):
    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    global movies
    action = 0
    loop = True
    
    while loop == True:
        action = display_menu()
        print(action)
        if action == 1:
            movies = add_movie(movies)
        if action == 2:
            view_movies(movies)
        if action == 5:
            loop = False
    # create the main menu loop
    # call the appropriate function based on the user's choice


main()