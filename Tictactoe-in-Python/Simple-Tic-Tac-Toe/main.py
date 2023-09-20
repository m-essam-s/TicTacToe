import random


def display_board(places):
    # The function accepts one parameter containing the places's current status
    # and prints it out to the console.
    # the horizontal line(bar) in the board   +-------+-------+-------+
    horizontal_line = "+-------" * 3 + "+\n"
    # the empty row  in the board             |       |       |       |
    empty_row = "|       " * 3 + "|\n"

    board = horizontal_line  # the board start's with the horizontal line(bar)
    for row in places:  # loop in all places valid or invalid
        board += empty_row  # adding empty row
        # dynamically adding moves to board
        board += "|   " + "   |   ".join(str(cell) for cell in row) + "   |\n"
        board += empty_row  # adding empty row
        board += horizontal_line  # adding horizontal line(bar) and so on
    print(board)                 # the board's current status


def user_move():
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    list_of_free_places = make_list_of_free_places(places)
    while True:
        try:
            move = int(input("Enter your move: "))
            if move in list_of_free_places:
                update_board(move, 'user')
                break
            elif move < 1 or move > 9:
                print("Out of range")
            else:
                print("Invalid move")
        except ValueError:
            print("Please enter a valid move")


def make_list_of_free_places(places):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_places = [
        cell for row in places for cell in row if cell in range(1, 10)]
    return free_places


def victory_for(places):
    # The function analyzes the board's status to check if a player using 'O's or 'X's has won the game
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combination in winning_combinations:
        symbols = [places[row][col] for row, col in combination]
        if symbols[0] == symbols[1] == symbols[2]:
            return "C" if symbols[0] == "X" else "U"

    return "No victory yet"


def computer_move():
    # The function draws the computer's move and updates the board.
    list_of_free_places = make_list_of_free_places(places)
    move = random.choice(list_of_free_places)
    print("Computer move: ", move)
    update_board(move, 'comp')


def update_board(move, player):

    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    row, col = mapping[move]
    places[row][col] = "O" if player == "user" else "X"


def check_winner():
    if victory_for(places) == "U":
        display_board(places)
        print("You won!")
        exit()
    elif victory_for(places) == "C":
        display_board(places)
        print("Computer won!")
        exit()
    else:
        "No victory yet"


if __name__ == "__main__":
    places = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]
    while True:
        display_board(places)
        user_move()
        display_board(places)
        computer_move()
        check_winner()
