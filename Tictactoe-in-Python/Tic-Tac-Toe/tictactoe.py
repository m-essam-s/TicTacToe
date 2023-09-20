import time
import os
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from gameplay import TicTacToe

"""
Tictactoe game using OOP
"""

def main(game, x_player, o_player, print_game=True, slow_game=True):
    if print_game:              #if print_game is set to True
        game.print_board_nums() #then print the game board with 
        time.sleep(.8)          #the placeholders within
    token = 'X' #the default first player is X

    # as long as there are still empty spots on the board, the 
    # player corresponding to the appropriate token is assigned
    while game.empty_spots():
        if token == 'X':
            spot = x_player.get_move(game)
        else: #spot=x_player.get_move(game) if token=='X' else o_player.get_move(game)
            spot = o_player.get_move(game)

        if game.make_move(spot, token):
            if print_game:
                print(f"{token} makes a move to spot {spot+1}") #this will print 1-9 instead of 0-8
                game.print_board()
                print('\n')
            
            if game.current_winner: # if the current_winner has been set to a token
                                    # since current_winner was initialized as None.
                if print_game:
                    print(f"{token} Wins!")
                return token #ends the loop and exits the game
            #alternate the tokens, switching the player who plas next
            token = 'O' if token == 'X' else 'X'

        time.sleep(0.8)  #a small break to make things easier to read
        if slow_game:
            time.sleep(0.8) #another break

    if print_game:
        print("It's a tie!")


if __name__ == "__main__":
    os.system("cls")
    print("\nWelcome to Tic-Tac-Toe!")
    mode = ' ' #initialised for while loop
    replay = 'Y' #initialised for while loop
    while mode not in ['A', 'B', 'C', 'D', 'E', 'F', 'X']:
        print("\nHow do you wish to play?")
        print("A. Player_1 VS Player_2")
        print("B. Player VS Easy_Computer")
        print("C. Player VS Genius_Computer")
        print("D. Easy_Computer VS Genius_Computer")
        print("E. Easy_Computer_1 VS Easy_Computer_2")
        print("F. Genius_Computer_1 VS Genius_Computer_2")
        print("\nX. Exit Game")
        mode = input("\n==> ").upper()
        
        if mode == 'X':
            break

        while replay == 'Y':
            if mode == 'A':
                print("\nPlayer_1 = X\nPlayer_2 = O\n")
                x_player = HumanPlayer('X')
                o_player = HumanPlayer('O')
                t = TicTacToe()
                main(t, x_player, o_player, print_game=True, slow_game=False)
            elif mode == 'B':
                choice = input("\nOK... Do you want to be X or O? ").upper()
                if choice == 'O':
                    print("\nEasy_Computer = X\nPlayer = O\n")
                    o_player = HumanPlayer('O')
                    x_player = RandomComputerPlayer('X')
                    t = TicTacToe()
                    main(t, x_player, o_player, print_game=True, slow_game=False)
                else:
                    print("\nPlayer = X\nEasy_Computer = O\n")
                    x_player = HumanPlayer('X')
                    o_player = RandomComputerPlayer('O')
                    t = TicTacToe()
                    main(t, x_player, o_player, print_game=True, slow_game=False)
            elif mode == 'C':
                choice = input("\nOK... Do you want to be X or O? ").upper()
                if choice == 'O':
                    print("\nGenius_Computer = X\nPlayer = O\n")
                    o_player = HumanPlayer('O')
                    x_player = GeniusComputerPlayer('X')
                    t = TicTacToe()
                    main(t, x_player, o_player, print_game=True, slow_game=False)
                else:
                    print("\nPlayer = X\nGenius_Computer = O\n")
                    x_player = HumanPlayer('X')
                    o_player = GeniusComputerPlayer('O')
                    t = TicTacToe()
                    main(t, x_player, o_player, print_game=True, slow_game=False)
            elif mode == 'D':
                print("\nSit Back, Relax and Enjoy the Show :)")
                time.sleep(2.5)
                print("Easy_Computer = X\nGenius_Computer = O\n")
                x_player = RandomComputerPlayer('X')
                o_player = GeniusComputerPlayer('O')
                t = TicTacToe()
                main(t, x_player, o_player, print_game=True, slow_game=True)
            elif mode == 'E':
                print("\nSit Back, Relax and Enjoy the Show :)")
                time.sleep(2.5)
                print("Easy_Computer = X\nEasy_Computer = O\n")
                x_player = RandomComputerPlayer('X')
                o_player = RandomComputerPlayer('O')
                t = TicTacToe()
                main(t, x_player, o_player, print_game=True, slow_game=True)
            elif mode == 'F':
                print("\nSit Back, Relax and Enjoy the Show :)")
                time.sleep(2.5)
                print("Genius_Computer = X\nGenius_Computer = O\n")
                x_player = GeniusComputerPlayer('X')
                o_player = GeniusComputerPlayer('O')
                t = TicTacToe()
                main(t, x_player, o_player, print_game=True, slow_game=True)
            else:
                print("Invalid choice. Try again")

            replay = input("\nDo you want to play again?(Y/N): ").upper()
            os.system("cls")
        #end of while loop

        mode = ' '
        replay = 'Y'        
    #end of while loop

    print("\n\n\n\n\t\tBye! Come Back Soon\n\n\n\n")
