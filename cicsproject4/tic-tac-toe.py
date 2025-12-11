# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500

def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(n):
    board=[]
    for i in range(n):
      rows=[" "]*n
      board.append(rows)
    return board


def get_location(n, board):
  while True:
    row_input = input(f"Please enter a row index between 0 and {n-1}: ")
    col_input = input(f"Please enter a column index between 0 and {n-1}: ")
    if not(row_input.isdigit() and col_input.isdigit()):
      print(f"({row_input}, {col_input}) is not a legal input!")
      continue
    row=int(row_input)
    col=int(col_input)
    if not(0<=row<n and 0<=col<n):
      print(f"({row}, {col}) is not a legal space!")
      continue
    if board[row][col] != " ":
      print(f"({row}, {col}) is not an available space!")
      continue
    return row, col


def row_win(n,board,person):
  for i in range(n):
    row_belongs=True
    for j in range(n):
      if board[i][j]!=person:
        row_belongs=False
        break
    if row_belongs==True:
      return True

  return False
  
def col_win(n,board,person):
  for i in range(n):
    col_belongs=True
    for j in range(n):
      if board[j][i]!=person:
        col_belongs=False
        break
    if col_belongs==True:
      return True

  return False

def diag_win(n,board,person):
  diag_belongs=True
  for i in range(len(board)):
      if board[i][i]!=person:
        diag_belongs=False
        break
  if diag_belongs==True:
    return True
  return False

def anti_diag_win(n,board,person):
  antidiag_belongs=True
  for i in range(len(board)):
      if board[i][(n-1)-i]!=person:
        antidiag_belongs=False
        break
  if antidiag_belongs==True:
    return True
  return False
      
def has_won(n,board,person):
  if(row_win(n,board,person)==True):
    return True
  elif(col_win(n,board,person)==True):
    return True
  elif(diag_win(n,board,person)==True):
    return True
  elif(anti_diag_win(n,board,person)==True):
    return True
  else:
    return False
     

def play_game(n):
  print(f"*** Welcome to {n} by {n} Tic-Tac-Toe ***")
  board = make_empty_board(n)
  print_board(n,board)
  count=0
  while True:
    if count%2==0:
      person="X"
      print(f"* {person}'s turn *")
      row, col=get_location(n,board)
      board[row][col] =person
      print_board(n,board)
      if has_won(n,board,person)==True:
        print(f"{person} wins!")
        break
      draw=True
      for i in range(len(board)):
        for j in range(len(board)):
          if board[i][j]==" ":
            draw=False
            break
        if draw==False:
          break
      count+=1
      if draw==True:
        print("Tie")
        break
      

    else:
      person="O"
      print(f"* {person}'s turn *")
      row, col=get_location(n,board)
      board[row][col] =person
      print_board(n,board)
      if has_won(n,board,person)==True:
        print(f"{person} wins!")
        break
      draw=True
      for i in range(len(board)):
        for j in range(len(board)):
          if board[i][j]==" ":
            draw=False
            break
        if draw==False:
          break
      count+=1
      if draw==True:
        print("Tie")
        break

play_game(4)


        