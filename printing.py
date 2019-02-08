
# Printing functions

from reports import*

user_input = int(input('Choose a number between 1-8: '))
if user_input == 1:
    print(count_games('game_stat.txt'))
if user_input == 2:
    print(decide('game_stat.txt', 2000))
if user_input == 3:
    print(get_latest('game_stat.txt', ))
if user_input == 4:
    print(count_by_genre('game_stat.txt', 'First-person shooter'))
if user_input == 5:
    print(get_line_number_by_title('game_stat.txt', 'Counter-Strike'))
if user_input == 6:
    print(sort_abc('game_stat.txt'))
if user_input == 7:
    print(get_genres('game_stat.txt'))
if user_input == 8:
    print(when_was_top_sold_fps('game_stat.txt'))