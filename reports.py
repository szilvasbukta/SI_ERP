
# Report functions


def count_games(file_name):

    with open(file_name, 'r') as f:
        counter = 0
        for line in f:
            counter += 1
        return counter


def decide(file_name, year):

    init_check = 0
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split('\t')
            game_info[4] = game_info[4].strip('\n')
            print(game_info[2])
            if int(game_info[2]) == year:
                init_check = 1
        if init_check == 1:
            return True
        else: 
            return False
