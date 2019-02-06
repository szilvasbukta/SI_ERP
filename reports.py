
# Report functions


def count_games(file_name):

    with open('file_name', 'r') as f:
        counter = 0
        for line in f:
            counter += 1
        return counter

