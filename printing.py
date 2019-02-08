
# Printing functions

from reports import *
def main():
    while True:
        user_input = int(input('''
1) Count_games   9) EXIT
2) Decide
3) Get_latest
4) Count_by_genre
5) Get_line_number_by_title
6) Sort_abc
7) Get_genres
8) When_was_top_sold_fps
\nChoose a function 1 - 8: '''))
        if user_input == 1:
            print("\nHow many games are in the file?\n")
            print("\n",count_games("game_stat.txt"),"\n")
        elif user_input == 2:
            print("\nIs there a game from a given year?\n")
            year = int(input("Choose a year: "))
            print("\n",decide("game_stat.txt", year),"\n")
        elif user_input == 3:
            print("\nWhich was the latest game?\n")
            print("\n",get_latest("game_stat.txt"),"\n")
        elif user_input == 4:
            print("\nHow many games do we have by genre?\n")
            genre = input("Choose a genre: ")
            print("\n",count_by_genre("game_stat.txt", genre),"\n")
        elif user_input == 5:
            print("\nWhat is the line number of the given game (by title)?\n")
            title = input("Choose a game title: ")
            print("\n",get_line_number_by_title("game_stat.txt", title),"\n")
        elif user_input == 6:
            print("\nWhat is the alphabetical ordered list of the titles?\n")
            for title in sort_abc('game_stat.txt'):
                print(title)
        elif user_input == 7:
            print("\nWhat are the genres?\n")
            for genre in get_genres('game_stat.txt'):
                print(genre)
        elif user_input == 8:
            print("\nWhat is the release date of the top sold 'First-person shooter' game?\n")
            print(when_was_top_sold_fps("game_stat.txt"),"\n")
        elif user_input == 9:
            exit()


if __name__ == "__main__":
    main()
