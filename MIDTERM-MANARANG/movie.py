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


def add_movie(movie_list):
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    pass


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
    action = 0
    loop = True
    
    while loop == True:
        action = display_menu()
        print(action)
        if action == 5:
            loop = False
    # create the main menu loop
    # call the appropriate function based on the user's choice


main()