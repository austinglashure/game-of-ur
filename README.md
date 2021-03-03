# game-of-ur
an old dice race game
AKA 'game of 20 squares'


described in this youtube video

https://www.youtube.com/watch?v=WZskjLq040I&ab_channel=TheBritishMuseum


Royal Game of Ur

  Build game board
    20 positions
    
  
  Create player object
    Pieces
      7 pieces a player
      each piece has a position
    Dice
      - 4 pointed and 4 dice
          each die can be either a 1 or a 0
      - 
    Moves
      - score cannot be subdivided betweein pieces
      - can move one piece as many tiles as there are points
      IF
        there is an enemy piece at your destination
          AND they aren't on the 'safe' tile:
            enemy piece gets knocked off and you occupy the piece
      ELIF 
      ELIF
        your piece occupies the destination tile
          INVALID move
      ELSE
        the destination is empty
          VALID move
      
  
  
