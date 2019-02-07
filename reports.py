
# Report functions


def count_games(file_name):

    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            count += 1
        return count


def decide(file_name, year):

    init_check = 0
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split('\t')
            game_info[4] = game_info[4].strip('\n')
            if int(game_info[2]) == year:
                init_check = 1
        if init_check == 1:
            return True
        else: 
            return False


def get_latest(file_name):

    latest_game = ['', 0]
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split('\t')
            game_info[2] = int(game_info[2])
            if game_info[2] > latest_game[1]:
                latest_game[1] = game_info[2]
                latest_game[0] = game_info[0]
        return latest_game[0]


def count_by_genre(file_name, genre):

    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            game_info = line.split('\t')
            if genre == game_info[3]:
                count += 1
        return count


def get_line_number_by_title(file_name, title):
    init_check = 0
    with open(file_name, 'r') as f:
        for x, line in enumerate(f):
            game_info = line.split('\t')
            if game_info[0] == title:
                init_check = 1
                line_number = x + 1
        if init_check == 1:
            return line_number
        else:
            raise ValueError


def sort_abc(file_name):

    ordered_titles = []
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split('\t')
            if len(ordered_titles) == 0 or (game_info[0]).lower() > (ordered_titles[len(ordered_titles) - 1]).lower():
                ordered_titles.append(game_info[0])
            else:
                for x, title in enumerate(ordered_titles):
                    if (game_info[0]).lower() < title.lower():
                        ordered_titles.insert(x, game_info[0])
                        break
        return ordered_titles


def get_genres(file_name):
    game_genres = []
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            line = line.split("\t")
            if (len(game_genres) == 0 or (game_genres[-1]).lower() < (line[3]).lower()) and line[3] not in game_genres:
                game_genres.append(line[3])
            elif line[3] not in game_genres:
                for x, title in enumerate(game_genres):
                    if (line[3]).lower() < title.lower():
                        game_genres.insert(x, line[3])
                        break
        return game_genres


def when_was_top_sold_fps(file_name):
    top_sold_game = [0, 0]
    check = 0
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split("\t")
            game_info[1] = float(game_info[1])
            game_info[2] = int(game_info[2])
            if game_info[1] > top_sold_game[1] and game_info[3] == 'First-person shooter':
                top_sold_game[0] = game_info[2]
                top_sold_game[1] = game_info[1]
                check = 1
        if check == 1:
            return top_sold_game[0]
        else:
            raise ValueError
