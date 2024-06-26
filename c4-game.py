# Doc in the code
SIZE = 10
FIRST = 1
SECOND = 2
EMPTY = 0
EXIT = -1


# Initializing the board
def init_board():
    matrix = []
    for row in range(SIZE):
        row_to_add = []
        for col in range(SIZE):
            row_to_add.append(EMPTY)
        matrix.append(row_to_add)
    return matrix


# Printing the board
def print_board(matrix):
    for row in range(SIZE):
        line_to_print = ''
        for col in range(SIZE):
            line_to_print += str(matrix[row][col]) + ' '
        print(line_to_print)


def get_cal_index(cal, board):
    for row_index in range(1, SIZE+1):
        if board[-row_index][cal - 1] == EMPTY:  # if the index is empty
            return -row_index, cal - 1
    return None


# Checking if the cal is valid
def is_valid_cal(cal, board):
    """
    Returns true if cal is valid and false if invalid.
    """
    # if index out of range
    if cal > SIZE or cal < 1:
        return False

    # if the cal is full
    if get_cal_index(cal, board) is None:
        return False

    return True


# Input player's move
def get_player_move(board):
    """
    :returns: the cal that chosen.
    """
    # input a cal until return
    while True:
        cal = int(input("Enter the column: "))

        # if input is exit
        if cal == EXIT:
            return EXIT
        # if the input is valid
        elif is_valid_cal(cal, board):
            return cal
        else:
            print("Wrong move, try again.")


def switch_player(current_player):
    if current_player == FIRST:
        return SECOND
    return FIRST


def check_raw(board, current_player):
    for row_index in range(SIZE):
        counter = 0
        for cal in range(SIZE):
            # if the player got this index
            if board[row_index][cal] == current_player:
                counter += 1
            # else, reset the counter
            else:
                counter = 0
            # if there is a sequence of this player
            if counter >= 4:
                return True
    return False


def check_cal(board, current_player):
    for cal_index in range(SIZE):
        counter = 0
        for row_index in range(SIZE):
            if board[row_index][cal_index] == current_player:
                counter += 1
            else:
                counter = 0
            if counter >= 4:
                return True
    return False


def is_winner(board, current_player):
    if check_raw(board, current_player):
        return True
    elif check_cal(board, current_player):
        return True
    return False


def get_player(player):
    """ A function to check player's name."""
    if player == FIRST:
        return "First"
    return "Second"


def main():
    # create the board
    board = init_board()
    current_player = FIRST

    # print the board
    print_board(board)
    total_turns = 0

    # while there are still cals left
    while total_turns < SIZE**2:
        print(get_player(current_player), "player -")
        # input a row from the player
        cal = get_player_move(board)
        # if input is exit
        if cal == EXIT:
            return EXIT

        # update in the board
        row, cal = get_cal_index(cal, board)
        board[row][cal] = current_player

        print_board(board)

        if is_winner(board, current_player):
            return print(get_player(current_player), "won!")

        # switch player
        current_player = switch_player(current_player)
        total_turns += 1

    print("The board is full, nobody wins")


main()
