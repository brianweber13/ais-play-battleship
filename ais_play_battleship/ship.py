""" contains both definition of ship and tests """

from copy import deepcopy

class Ship:
    """ describes one ship in the game """

    # constructor
    def __init__(self, ship_info):
        """ creates a ship

        Keyword arguments:
        ship_info -- Required attributes:
                        name (str): name (aka type) of ship, such as 'carrier'
                                    or 'battleship'
                        occupied_squares (list of tuple): ship's location on
                                    the board.
                        length (int): size of ship
                     Optional attributes: 
                        placed (bool): whether or not ship has been placed
                        sunk (bool): whether or not ship has been sunk

                     unhit_squares is constructed
                     from occupied_squares, and it shrinks as the ship is
                     hit. When it is empty, the ship has sunk.
        """

        self.name = ship_info['name']
        self.length = ship_info['length']
        self.occupied_squares = ship_info['occupied_squares']
        self.unhit_squares = deepcopy(self.occupied_squares)
        if hasattr(ship_info, 'sunk'):
            self.sunk = ship_info.sunk
        else:
            self.sunk = False
        if hasattr(ship_info, 'placed'):
            self.placed = ship_info.placed
        else:
            self.placed = False

    def check_for_hits(self, coordinate):
        """ checks if a square is a hit on THIS SHIP. If it is, removes that
        square from unhit_squares.
 
        Args:
            coordinate (tuple): location to check
        """
        if coordinate in self.occupied_squares:
            self.unhit_squares.discard(coordinate)
            if self.check_if_sunk():
                self.sunk = True
            return True
        return False

    def check_if_sunk(self):
        """ checks if ship has been sunk """
        return not self.unhit_squares

    # basically a toString function. If I call print(Ship), this is what will
    # happen.
    def __str__(self):
        info = 'Name:             ' + str(self.name) + '\n'
        info += 'Length:           ' + str(self.length) + '\n'
        info += 'Occupied Squares: ' + str(self.occupied_squares) + '\n'
        info += 'Un-hit Squares:   ' + str(self.unhit_squares) + '\n'
        info += 'Sunk:             ' + str(self.sunk) + '\n'
        info += 'Placed:           ' + str(self.placed)
        return info

# tests: will be run by running this script from the command line
def main():
    """ create a test ship, and then do the following:

    - print it
    - shoot it (expect a hit)
    - shoot it again (expect a miss)
    - check if it's sunk (expect it to not be sunk)
    - shoot it until it sinks
    - check if it's sunk (expect it to be sunk)

    Ship.placed is not tested because that is only used in game.py
    """
    test_ship = Ship({
        'name': 'carrier',
        'length': 5,
        'occupied_squares': set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
        })
    print('Original Ship: ')
    print(test_ship)
    print('')

    print('shooting ship at 3, 0 (will output true if this is a hit.)')
    print(test_ship.check_for_hits((3, 0)))
    print(test_ship)
    print('')

    print("""shooting ship at 3, 0 (will output true, but not change
            unhit_squares.)""")
    print(test_ship.check_for_hits((3, 0)))
    print(test_ship)
    print('')

    print('is ship sunk?')
    print('method says:    ', test_ship.check_if_sunk())
    print('attribute says: ', test_ship.sunk)
    print('')

    print('sinking the ship!')
    test_ship.check_for_hits((0, 0))
    test_ship.check_for_hits((1, 0))
    test_ship.check_for_hits((2, 0))
    test_ship.check_for_hits((4, 0))
    print(test_ship)
    print('')

    print('is ship sunk?')
    print('method says:    ', test_ship.check_if_sunk())
    print('attribute says: ', test_ship.sunk)

if __name__ == '__main__':
    main()
