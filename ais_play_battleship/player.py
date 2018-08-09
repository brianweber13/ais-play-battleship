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
    def __init__(self, board_size, ships):
        self.board =
        # radar is what you know about the enemy. This is where known hits and
        # misses are marked
        self.radar =
        self.ships =
        self.all_ships_are_sunk =

    # def all_ships_are_sunk(self):
    #     for ship in self.ships:
    #         if (ship.sunk == False):
    #             return False
    #     return True

# tests go here
def main():
    test_player = Player(10, [Ship({
                                    'name': 'carrier',
                                    'length': 5,
                                    'occupied_squares': set([(0, 0), (1, 0),
                                                             (2, 0), (3, 0),
                                                             (4, 0)]),
                                    }),
                              Ship({
                                    'name': 'battleship',
                                    'length': 4,
                                    'occupied_squares': set([(0, 1), (1, 1),
                                                             (2, 1), (3, 1),
                                                             (4, 1)]),
                                    })])

if __name__ == '__main__' :
    main()
