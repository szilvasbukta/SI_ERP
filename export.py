
# Export functions
from reports import*

with open('export_file.txt', 'w') as f:
    f.write(str(count_games('game_stat.txt')))
    f.write('\n')
    f.write(str(decide('game_stat.txt', 2000)))
    f.write('\n')
    f.write(str(get_latest('game_stat.txt')))
    f.write('\n')
    f.write(str(count_by_genre('game_stat.txt', 'First-person shooter')))
    f.write('\n')
    f.write(str(get_line_number_by_title('game_stat.txt', 'Counter-Strike')))
    f.write('\n')
    f.write(str(sort_abc('game_stat.txt')))
    f.write('\n')
    f.write(str(get_genres('game_stat.txt')))
    f.write('\n')
    f.write(str(when_was_top_sold_fps('game_stat.txt')))
