#Kamil Ahmed

#-----Global Variables----

#gameboard

#if game_still_going
game_still_going = True

#who won?
winner = None 

#who's turn is it?

current_player = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#display the board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#play a game of Tic Tac Toe
def play_game():
  
  #display initial code 
  display_board()
  
  #create a while loop as the game continues
  while game_still_going:
    
    #handle a single turn of an arbitrary player
    handle_turn(current_player)

    #check if the game is over
    check_if_game_over()

    #flip to the other player
    flip_player()

# the game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

#handle a single turn of an arbitrary player
def handle_turn(player):
  


  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
        valid = True
    else:
      print("You can't go there. Go again.")
  
   
 
  board[position] = player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  #setup global variables
  global winner 
  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  # check diagnols
  diagnol_winner = check_columns()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagnol_winner:
    winner = diagnol_winner
  else:
    winner = None
  return

def check_rows():
  #setup global variable
  global game_still_going
  #check if any of the rows have the same value
  #and is not empty
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  #if this rows have a match then there is a win
  #return the winner X or O
  if row_1 or row_2 or row_3:
    game_still_going = False
  return
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  #setup global variable
  global game_still_going
  #check if any of the column have the same value
  #and is not empty
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  #if this column have a match then there is a win
  #return the winner X or O
  if column_1 or column_2 or column_3:
    game_still_going = False
  return
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  
  return

def check_diagnols():
  #setup global variable
  global game_still_going
  #check if any of the column have the same value
  #and is not empty
  diagnols_1 = board[0] == board[4] == board[8] != "-"
  diagnols_2 = board[6] == board[4] == board[2] != "-"
  

  #if this column have a match then there is a win
  #return the winner X or O
  if diagnols_1 or diagnols_2:
    game_still_going = False
  return
  if diagnols_1:
    return board[0]
  elif diagnols_2:
    return board[6]
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False 
  return

def flip_player():
  global current_player
  #if current player was X change to O
  if current_player == "X":
    current_player = "O"
  #current player was O change to X
  elif current_player == "O":
    current_player = "X"
  return

play_game()