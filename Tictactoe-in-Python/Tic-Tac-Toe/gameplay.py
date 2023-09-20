"""
Functions that define the actual gameplay processes,
boards as well as the turns
"""

class TicTacToe:
    def __init__ (self):
        self.board = [' ' for _ in range(9)] #list to represent 3x3 board
        self.current_winner = None  #keeps track of whether there has been a winner or not.
    
    def print_board (self): #an empty board
        print("\n\t\t-------------")
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print("\t\t| " + ' | '.join(row) + " |\n\t\t-------------")

    @staticmethod
    def print_board_nums(): #board with placeholder
        # now we determine which number corresponds with which spot
        # e.g | 0 | 1 | 2 |, but add 1 to each i.e | 1 | 2 | 3 |
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print("\n\t\t-------------")
        for row in number_board:
            print("\t\t| " + ' | '.join(row) + " |\n\t\t-------------")
        print('\n')
    
    # To know the available moves after every turn
    def available_moves(self): #returns a list of indices of the available spots
        return [i for i,spot in enumerate(self.board) if spot == ' ']

        # This list comprehension basically expands to the below:
        #moves = []
        #for (i,spot) in enumerate(self.board):
        #    if spot == ' '
        #        moves.append(i)
        
    def empty_spots(self): #checks if there ar empty spots on the board
        return ' ' in self.board
        #boolean that returns true if there are free spots
        
    def num_empty_spots(self): #returns the number of available moves left on board
        return len(self.available_moves())
        # this can also be done with math module:
        #return self.board.count(' ')

    def make_move(self, spot, token):
        #if the move is valid, make the move and return true
        if self.board[spot] == ' ':  # if spot on board is empty
            self.board[spot] = token # then assign the next token there

            #check if someone won the game after their turn and who it is.
            if self.winner(spot, token):    # if the game has been won,
                self.current_winner = token # The current_winner takes the token
                                            # of the player that played last
            return True
        return False

    #checks if the game has been won and defines how it happens
    def winner(self, spot, token):
    
        #check rows
        row_index = spot // 3   # all 3 elements along the same row 
                                # should have the same whole number 
                                # division of 3 (i.e 0//3 == 1//3 == 2//3 == 0) 
        row = self.board[row_index*3 : (row_index+1)*3]
        #given the index, get the row i.e print('row', row)
        if all([r==token for r in row]): #all spots in a row have a particular token
            return True

        #check columns
        col_index = spot % 3    # all 3 elements along the same column
                                # should have the same value of modulus 3 
                                # (i.e 0%3 == 3%3 == 6%3 == 0) 
        column = [self.board[col_index + i*3] for i in range(3)] #print('col', col)
        if all ([c==token for c in column]):
            return True

        #checks diagonals
        # the diagonal spots are all occupied by 
        # the even numbers across the board, from 0-8
        if spot % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #diagonal left-to-right
            if all([d == token for d in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #diagonal right-to-left
            if all([d == token for d in diagonal2]):
                return True
        return False #this is unecessary though
