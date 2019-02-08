
# Export functions

from reports import *

with open('export_file.txt', "w") as opened_file:
    opened_file.write(str(count_games("game_stat.txt")))
    opened_file.write("\n")
    opened_file.write(str(decide("game_stat.txt", 2000)))
    opened_file.write("\n")
    opened_file.write(str(get_latest("game_stat.txt")))
    opened_file.write("\n")
    opened_file.write(str(count_by_genre("game_stat.txt", "First-person shooter")))
    opened_file.write("\n")
    opened_file.write(str(get_line_number_by_title("game_stat.txt", "Counter-Strike")))
    opened_file.write("\n")
    opened_file.write(str(sort_abc("game_stat.txt")))
    opened_file.write("\n")
    opened_file.write(str(get_genres("game_stat.txt")))
    opened_file.write("\n")
    opened_file.write(str(when_was_top_sold_fps("game_stat.txt")))
