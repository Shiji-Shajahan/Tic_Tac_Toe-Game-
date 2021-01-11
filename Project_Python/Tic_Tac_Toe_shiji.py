import random
EMPTY_SLOT = "-"
X_PLAYER = "X"
O_PLAYER = "0"
TIE = "tie"


WIN_COMBINATION_INDICES = [
  # Complete row
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Complete column
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Complete diagonal
  [0, 4, 8],
  [2, 4, 6]
]

def initialize_board():
  board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
  return board


def display_board(board):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

#print(display_board(board))

def valid_position(position, board):
  valid_location=["1","2","3","4","5","6","7","8","9"]
    
  if position not in valid_location:
    print('You have entered a wrong position, try another valid position')
  elif board[int(position) -1] == EMPTY_SLOT:
    return True
  else:
    print('This position is already occupied, try another position')

   # TODO Check if the position is a number between 1 and 9 AND if it is empty (EMPTY_SLOT)
  return False
  
def handle_turn(player, board):
  print(f"{player}, it's your turn.")
  position=input("Enter a valid position on board")

  valid = valid_position(position, board)
  # TODO Ask player to input a position (1-9). Ask while the position is not valid (check using valid_position)
  while not valid:
    position=input(" Enter a valid position on board")
    valid = valid_position(position, board)
  # TODO Write player's sign in board
  position=int(position)-1
  board[position]=player
  
  return board

def switch_player(player):
  # TODO Switch the player: X --> 0 or 0 --> X
  if player==X_PLAYER:
    player=O_PLAYER

  elif player==O_PLAYER:
    player=X_PLAYER

  return player

def choose_player(player):
  player=['X', '0']
  return (random.choice(player))


def check_for_winner(board):
  winner = None
  
  # Check if any of the players got a win combination
  for comb in WIN_COMBINATION_INDICES:
    if board[comb[0]] == board[comb[1]] == board[comb[2]] == X_PLAYER:
      winner = X_PLAYER
    elif board[comb[0]] == board[comb[1]] == board[comb[2]] == O_PLAYER:
      winner = O_PLAYER
    
  # TODO Check if any of the players got a win combination
  # Hint: loop over WIN_COMBINATION_INDICES to check if one of the combination is X-X-X or O-O-O

  # TODO If there is no winner, check if all spots are filled already. This would mean tie (winner = TIE)
  # Hint: count number of filled slots
  
  if EMPTY_SLOT not in board:
    winner=TIE

  return winner


def tic_tac_toe():
  winner = None
  player= None
  filled_slots=0
  game_still_going = True
  player = choose_player(player)
  # X will start. TODO (optional): select who starts randomly --> do this in a separate function

  # Initialize board
  board = initialize_board()
  
  while game_still_going:
  # TODO run this while the game is still going
    # Display board
    print(display_board(board))


    # Ask the player for a valid position and write it on the board
    board = handle_turn(player, board)
    print(board)
    
    player=switch_player(player)
    # Check if there is a winner already
    
    filled_slots+=1
    print("filled_slots is",filled_slots)
    
    winner = check_for_winner(board)
    print("The winner is", winner)

    # TODO stop the game if there is a winner, otherwise switch the player

    if winner !=None:
      game_still_going=False
    

  print("THE END")
  if winner == TIE:
      print("Tie")
  else:
      print(f"Congratulations {winner}!!")
  display_board(board)


# Start game
tic_tac_toe()
