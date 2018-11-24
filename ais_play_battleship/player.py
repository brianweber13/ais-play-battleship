# holds data used by game.py. Number and types of ships, whether or not ships
# are sunk, and size of board is all given by the game object

import ship

### CONSTANTS ###
SQUARE_EMPTY = 0
SQUARE_SHIP  = 1
SQUARE_MISS  = 2
SQUARE_HIT   = 3
SQUARE_SUNK  = 4

class Player:
    def __init__(self, ships, board_size=10):
        """ 
        Keyword arguments
        ships (list): all the ships this player has.
        board_size (int): size of board (board sizes much match between
            players. All boards are square)
        """
        # radar is what you know about the enemy. This is where known hits and
        # misses are marked
        self.board, self.radar = [[SQUARE_EMPTY] * board_size] * board_size
        self.ships = ships
        self.all_ships_are_sunk = False

    # def all_ships_are_sunk(self):
    #     for ship in self.ships:
    #         if (ship.sunk == False):
    #             return False
    #     return True
