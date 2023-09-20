import random
import math

"""
functions that define characteristics of different players.
It allows human players as well as random computer players.
"""

class Player:
    def __init__(self, token):  # token is either 'X' or 'O'
        self.token = token

    def get_move (self, game):
        pass

class HumanPlayer(Player):
    def __init__ (self, token):
        super().__init__(token)
    
    def get_move (self, game):
        # these attributes are initialized for the loop
        valid_spot = False  # is the chosen spot available?
        move = None

        while not valid_spot:  # while valid_spot is still false
            spot = input(f"{self.token}'s turn. Input move (1-9): ")
            print('\n')
        
            try:
                move = int(spot)-1  # since user will input 1-9 instead of 0-8
                # if the spot chosen is valid, then 
                # set attr. valid_spot to True
                if move not in game.available_moves():
                    raise ValueError
                valid_spot = True
            
            except ValueError:
                print("Invalid spot. Try again\n")
        
        return (move)

class RandomComputerPlayer(Player):
    def __init__ (self, token):
        super().__init__(token)
    
    def get_move (self, game):
        # the computer selects a random spot on the board
        # out of the available spaces and returns the index
        # as its spot
        spot = random.choice(game.available_moves())
        return spot

class GeniusComputerPlayer(Player):  # computer using minimax
    def __init__ (self, token):
        super().__init__(token)

    def get_move(self, game):
        if len(game.available_moves()) == 9:  # first move is random if board is free
            spot = random.choice(game.available_moves())
        else:
            spot = self.minimax(game, self.token)['position']  # this is because minimax
                                                    # returns a dictionary with both position 
                                                    # and score keys but we only need the value 
                                                    # on the position
        return spot

    # minimax outputs a dictionary containing the best possible postion after analysis
    #  and the score attached to that position according to the analysis made.
    #  The analysis uses the formula 1(x+1) or -1(x+1) or 0(x+1) depending on whether
    #  the first person computer is winning, losing or drawing respectively.

    def minimax(self, state, player):    # state here means the condition (screenshot)
                                        # of the game at that particular point in time
        # assign tokens
        max_player = self.token  # this is whatever token player uses,
                                # so max_player is the first person computer
        other_player = 'O' if player == 'X' else 'X'  # the opponent

        # Now we have to consider two situations (base cases) before playing here.
        # if any of these happens then we don't need to continue with the algorithm,
        # we can just return from the function the corresponding return values required.

        # 1. The opponent won in the previous move
        if state.current_winner == other_player:
            return {'position': None,     # the best position for us to play in
                    'score': (1*(state.num_empty_spots()+1)) if other_player == max_player
                              else (-1*(state.num_empty_spots()+1))}

        # 2. Game is presently a draw (no empty spots)
        elif not state.empty_spots():
            return {'position': None,
                    'score': 0}  # 0(x+1)

        # initializing
        if player == max_player:
            best = {'position': None,
                    'score': -math.inf}  # each score should maximize (be larger)
                                        # using -ve infinity here ensures that.
        else:  # player == other_player
            best = {'position': None,
                    'score': +math.inf}  # each score should minimixe (be smaller)
                                        # using +ve infinity here ensures that.

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot)
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax (state, other_player)  # sim_score is a dictionary that stores
                                                # the position and score results from the simulation

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # otherwise this will get messed up from the recursion

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score #replace best
            else: #if player == other_player
                if sim_score['score'] < best['score']:
                    best = sim_score #replace best

        #end of for loop
        return best # {'postion':  , 'score':  }