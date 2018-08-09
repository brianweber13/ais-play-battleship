# Rules of the Game:
[Sorce](https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm)
## Game Objective
The object of Battleship is to try and sink all of the other player's ships
before they sink all of your ships. All of the other player's ships are
somewhere on his/her board. You try and hit them by calling out the
coordinates of one of the squares on the board. The other player also tries to
hit your ships by calling out coordinates. Neither you nor the other player
can see the other's board so you must try to guess where they are. Each board
in the physical game has two grids: the lower (horizontal) section for the
player's ships and the upper part (vertical during play) for recording the
player's guesses.

## Starting a New Game
Each player places the 5 ships somewhere on their board. The ships can only be
placed vertically or horizontally. Diagonal placement is not allowed. No part
of a ship may hang off the edge of the board. Ships may not overlap each
other. No ships may be placed on another ship. 

Once the guessing begins, the players may not move the ships.

The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3),
Submarine (3), and Destroyer (2). 

## Playing the Game
Player's take turns guessing by calling out the coordinates. The opponent
responds with "hit" or "miss" as appropriate. Both players should mark their
board with pegs: red for hit, white for miss. For example, if you call out F6
and your opponent does not have any ship located at F6, your opponent would
respond with "miss". You record the miss F6 by placing a white peg on the
lower part of your board at F6. Your opponent records the miss by placing.

When all of the squares that one your ships occupies have been hit, the ship
will be sunk. You should announce "hit and sunk". In the physical game, a
red peg is placed on the top edge of the vertical board to indicate a sunk
ship. 

As soon as all of one player's ships have been sunk, the game ends.

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

