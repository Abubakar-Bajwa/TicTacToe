import random
def winner(board):
# Check rows for winner
  for row in range(3):
    if (board[row][0] == board[row][1] == board[row][2]) and\
(board[row][0] != " "):
      return board[row][0]
# Check columns for winner
  for col in range(3):
    if (board[0][col] == board[1][col] == board[2][col]) and\
  (board[0][col] != " "):
      return board[0][col]

# Check diagonal (top-left to bottom-right) for winner
  if (board[0][0] == board[1][1] == board[2][2]) and\
  (board[0][0] != " "):
    return board[0][0]
# Check diagonal (bottom-left to top-right) for winner
  if (board[2][0] == board[1][1] == board[0][2]) and\
  (board[2][0] != " "):
    return board[2][0]
# No winner: return the empty string
  return ""
def display_board(board):
  print(" 0 1 2")
  print("0: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
  print(" ---+---+---")
  print("1: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
  print(" ---+---+---")
  print("2: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
  print()


def make_user_move(board):
  valid_move = False
  isCorrect = False
  while not valid_move:
    while not isCorrect:
      try:
        row = int(input("What row would you like to move to (0-2):"))
        isCorrect = True
      except ValueError:
        print("please enter a number")
        
    isCorrect = False
    while not isCorrect:
      try:  
        col = int(input("What col would you like to move to (0-2):"))
        isCorrect = True
      except ValueError:
        print("please enter a number")
    if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "):
      board[row][col] = 'X'
      valid_move = True
    else:
      print("Sorry, invalid square. Please try again!\n")
def make_user2_move(board):
  valid_move = False
  isCorrect = False
  while not valid_move:
    while not isCorrect:
      try:
        row = int(input("What row would you like to move to (0-2):"))
        isCorrect = True
      except ValueError:
        print("please enter a number")

    isCorrect = False
    while not isCorrect:
      try:  
        col = int(input("What col would you like to move to (0-2):"))
        isCorrect = True
      except ValueError:
        print("please enter a number")
    if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "):
      board[row][col] = 'O'
      valid_move = True
    else:
      print("Sorry, invalid square. Please try again!\n")

def make_computer_move(board):
  valid_move = False
  while not valid_move:
    row = random.randint(0,2)
    col = random.randint(0,2)
    if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "):
      board[row][col] = 'O'
      valid_move = True

def main():
  """Our Main Game Loop:"""
  free_cells = 9
  users_turn = True
  ttt_board = [ [ " ", " ", " " ], [ " ", " ", " " ], [ " ", " ", " " ] ]
  while winner(ttt_board) == "" and (free_cells > 0):
    display_board(ttt_board)
    if users_turn:
      make_user_move(ttt_board)
      users_turn = not users_turn
    else:
      make_user2_move(ttt_board)
      users_turn = not users_turn
      free_cells -= 1
      display_board(ttt_board)
  if (winner(ttt_board) == 'X'):
    print("User 1 won!")

  elif (winner(ttt_board) == 'O'):
    print("User 2 won")
  else:
    print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")
# Start the game!
main()
