import player

### CONSTANTS ###
AI1 = 1
AI2 = 2

DEFAULT_STARTING_SHIPS = [
    {
        'type': 'carrier',
        'length': 5,
        'quantity_available': 1,
        'occupied_squares': [],
        'sunk': False,
    },
    {
        'type': 'battleship',
        'length': 4,
        'quantity_available': 1,
        'occupied_squares': [],
        'sunk': False,
    },
    {
        'type': 'destroyer',
        'length': 3,
        'quantity_available': 1,
        'occupied_squares': [],
        'sunk': False,
    },
    {
        'type': 'submarine',
        'length': 3,
        'quantity_available': 1,
        'occupied_squares': [],
        'sunk': False,
    },
    {
        'type': 'patrol boat',
        'length': 2,
        'quantity_available': 1,
        'occupied_squares': [],
        'sunk': False,
    }
]

### Game object ###
class Game:
    # Game constructor
    def __init__(self, ai1 = player(), ai2 = player(), board_size = 10, starting_ships = DEFAULT_STARTING_SHIPS):
        self.game_over = False
        # ais must inherit from the Player class
        self.ai1 = ai1
        self.ai2 = ai2
        self.starting_board = [[SQUARE_EMPTY for i in board_size] for i in board_size]
        self.starting_ships = starting_ships
        self.ai1.board, self.ai1.enemy_board, self.ai2.board, self.ai2.enemy_board = self.starting_board
        self.ai1.ships, self.ai2.ships = self.starting_ships
    # target_square is a tuple
    def shoot(self, source_player, target_player, target_square):
        x = target_square[0]
        y = target_square[1]
        if target_player.board[x][y] = SQUARE_EMPTY:
            source_player.enemy_board[x][y] = SQUARE_MISS
        elif target_player.board[x][y] = SQUARE_SHIP:
            source_player.enemy_board[x][y] = SQUARE_HIT
            label_newly_sunk_ships(target_player, source_player.enemy_board,
                    target_square):
        pass
    # returns ID of the winner
    def game_is_over(self):
        if self.ai1.all_ships_are_sunk():
            return AI2
        elif self.ai2.all_ships_are_sunk():
            return AI1
        else:
            return 0

    def label_newly_sunk_ships(self, player_with_ships_to_check, board_to_check,
            location_to_check):
        for ship in player_with_ships_to_check.ships:
            if location_to_check in ship.occupied_squares:
                ship_is_sunk = True
                for occupied_square in ship.occupied_squares:
                    x = occupied_square[0]
                    y = occupied_square[1]
                    if board_to_check[x][y] != SQUARE_HIT:
                        ship_is_sunk = False
                if ship_is_sunk:
                    for occupied_square in ship.occupied_squares:
                        x = occupied_square[0]
                        y = occupied_square[1]
                    # TODO: test this stuff below
                    board_to_check[x][y] = SQUARE_SUNK # will this modify original board or a copy of it????


    def play(self):
        pass
