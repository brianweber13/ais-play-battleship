# Objects:

## Ship
### Attributes:
* str: name/type of ship
* int: length (number of squares occupied)
* list of tuples: occupied squares
* list of tuples: hit squares (only contains occupied squares that have already
  been hit, NOT all the hit squares on the board)
* bool: sunk?
* bool: placed?

### Methods:
* check for hit

### Other Notes:
* a ship belongs to a player

## Player
### Attributes:
* str: name of ai (for storing statistics)
* 2d matrix: radar (what you know about the location of enemy ships: What shots
  have been misses and what shots have been hits)
* 2d matrix: board (where your own ships are located)
* list of ships: own ships
* bool: all ships sunk?

### Methods:
* check for hit (on own board)
  * then update which ships are sunk
* shoot

### Other Notes:
* AIs built by people will inherit from this class

## Game
The "organizer" or "game master". Makes sure each ai takes turns and controls
when the game starts and ends. Declares a winner. Can run multiple games.

### Methods:
* play game
  * randomize who goes first (or in case of multiple games, take turns
    going first)
  * request for each AI to shoot, then report if it was a hit or a miss
  * if all ships are sunk then the game ends and person with ships remaining
    wins
  * repeat x number of times, store statistics (lifetime, this session, etc...)
Note: this will be split into smaller sub functions as it becomes clearer what
parts can be isolated. For now I'm just going to move forward.

