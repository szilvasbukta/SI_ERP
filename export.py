
# Export functions

from reports import *


def main():
    needed_file = input("\nChoose a file where to export: ")
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
        with open(needed_file+".txt", "a") as opened_file:
            if user_input == 1:
                print("\nHow many games are in the file?\n")
                opened_file.write("How many games are in the file: "+str(count_games("game_stat.txt"))+"\n")
            elif user_input == 2:
                print("\nIs there a game from a given year?\n")
                year = int(input("Choose a year: "))
                opened_file.write("Is there a game from a given year("+str(year)+"): "+str(decide("game_stat.txt", year))+"\n")
            elif user_input == 3:
                print("\nWhich was the latest game?\n")
                opened_file.write("Which was the latest game: "+str(get_latest("game_stat.txt"))+"\n")
            elif user_input == 4:
                print("\nHow many games do we have by genre?\n")
                genre = input("Choose a genre: ")
                opened_file.write("How many games do we have by genre("+genre+"): "+str(count_by_genre("game_stat.txt", genre))+"\n")
            elif user_input == 5:
                print("\nWhat is the line number of the given game (by title)?\n")
                title = input("Choose a game title: ")
                opened_file.write("What is the line number of the given game by title("+title+"):"+str(get_line_number_by_title("game_stat.txt", "Counter-Strike"))+"\n")
            elif user_input == 6:
                print("\nWhat is the alphabetical ordered list of the titles?\n")
                opened_file.write("\nWhat is the alphabetical ordered list of the titles?\n")
                for title in sort_abc('game_stat.txt'):
                    opened_file.write(title+"\n")
            elif user_input == 7:
                print("\nWhat are the genres?\n")
                opened_file.write("\nWhat are the genres:\n")
                for genre in get_genres('game_stat.txt'):
                    opened_file.write(genre+"\n")
            elif user_input == 8:
                print("\nWhat is the release date of the top sold 'First-person shooter' game?\n")
                opened_file.write("What is the release date of the top sold 'First-person shooter' game: "+str(when_was_top_sold_fps("game_stat.txt"))+"\n")
            elif user_input == 9:
                exit()


if __name__ == "__main__":
    main()