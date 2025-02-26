# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Raquel Susko, Gabi Eguizabal, Emily Haddad, Neela Rajesh, Jojo Owens
# Section:      ENGR 102 - 213
# Assignment:   Lab 13- Team
# Date:         12/1/23


'''

Display the rules of the game and instructions for the user
• Display a set of options for the various things your players can do (display instructions, display
score, quit early, etc)
• Use at least one if-elif-else statement
• Use at least one loop
• Write at least three functions with docstrings
• Use at least one try-except block for something
• Use file input/output for something
• Use turtle graphics to draw something
• Incorporate at least one thing beyond what is covered in the lectures (learn something new)
• Be creative and have fun

'''
# Import modules Used 
import turtle as t
import random as r

# Instruction and option Functions
def display_instructions():
    '''prints the game's instructions to the console'''
    print("This is a 2 player game that uses a 5x5 board.")
    print("There are four black (B) pieces and four red (R) pieces. Black goes first.")
    print("Players take turns placing their pieces on empty spaces on the grid.")
    print("The goal is to get four in a line (horizontal, vertical, or diagonal) or in a square composed of markers in four adjacent spaces")
    print("Once the 8 pieces are initially placed, players can only move their pieces to adjacent empty spaces.")


def display_options():
    '''prints player's options to the console'''
    print("To quit the game, enter 'q'")
    print("To display the instructions, enter 'r'")
    print("To see your options, enter 'o'")
    print("To display the board, enter 'd'")
    print("To enter a move, enter the coordinates separated by a space ex: 5 5")

# File Function 
def read_board_file():
    '''reads in the board from a file and return a 2D list for the empty board'''
    board = []
    input_file = open("board.txt", "r")
    for i in range(5):
        board.append(input_file.readline().split(' '))
    return board

# Display board
def display_board():
    '''prints the board to the console''' 
    for line in board:
        print(" ".join(line))

# Move functions 
def get_move_initial():
    '''gets coordinates from user while pieces are still being place, checks if coordinates valid, asks for new coordinates if not valid
        returns coordinates as a list'''
    isValid = False
    while isValid == False:
        try:
            move = input("Enter your coordinates or a command: ")
            move = [int(num)-1 for num in move.split()]
            if not (0<=move[0]<=4) or not (0<=move[1]<=4) or board[move[0]][move[1]] != ".":
                raise Exception()
            else:
                isValid = True
        except:
            if not(move == "r" or move == "o" or move == "q" or move == "d"):
                print("That input was not valid! Please enter a coordinate between 1-5 for an empty spot or r,o,q,d!")
            else:
                isValid = True
    return move


def get_moves(board, player):
    '''gets coordinates from user after all pieces placed, checks if coordinates valid, asks for new coordinates if not valid
        returns coordinates as a list'''
    isValid = False
    while isValid == False:
        try:

            move = input("Enter your coordinates or command: ")
            move = [int(num)-1 for num in move.split()]
            if not (0<=move[0]<=4) or not (0<=move[1]<=4) or board[move[0]][move[1]] != ".":
                raise Exception()
            else:
                old_move = input("Enter the coordinates of the piece you want to move: ")
                old_move = [int(num)-1 for num in old_move.split()]
                if abs(old_move[0]-move[0]<=1) and abs(old_move[1]-move[1]<=1) and board[old_move[0]][old_move[1]]==player:
                    board[old_move[0]][old_move[1]] = "."
                    isValid = True
                else:
                    raise Exception()
        except:
            if not(move == "r" or move == "o" or move == "q" or move == "d"):
                print("That input was not valid! Please enter a coordinate between 1-5 for an empty spot or r,o,q,d!")
                print("Remember you can only move your player to an adjacent empty space!")
            else:
                isValid = True
    return move

# Checking if there are four in a row or a square functions
def check_sides(coord, player):
  '''checks if 4 in a row to the left and/or right of placed piece, returns true if 4 in a row'''
  count = 0
  try:
      i=1
      while board[coord[0]][coord[1]-i] == player:
          count+=1
          i+=1
  except:
      pass
  try:
      i=1
      while board[coord[0]][coord[1]+i] == player:
          count+=1
          i+=1
  except:
      pass
  return (count+1)==4


def check_top_bottom(coord, player):
  '''checks if 4 in a row to the top and/or bottem of placed piece, returns true if 4 in a row'''
  count = 0
  try:
      i=1
      while board[coord[0]-i][coord[1]] == player:
          count+=1
          i+=1
  except:
      pass
  try:
      i=1
      while board[coord[0]+i][coord[1]] == player:
          count+=1
          i+=1
  except:
      pass
  return (count+1)==4


def check_diagonals(coord, player):
  '''checks if 4 in a row diagonally, returns true if 4 in a row'''
  count1 = 0
  try:
      i=1
      while board[coord[0]-i][coord[1]-i] == player:
          count1+=1
          i+=1
  except:
      pass
  try:
      i=1
      while board[coord[0]+i][coord[1]+i] == player:
          count1+=1
          i+=1
  except:
      pass

  count2 = 0
  try:
      i=1
      while board[coord[0]-i][coord[1]+i] == player:
          count2+=1
          i+=1
  except:
      pass
  try:
      i=1
      while board[coord[0]+i][coord[1]-i] == player:
          count2+=1
          i+=1
  except:
      pass
  return (count1+1)==4 or (count2+1)==4


def check_squares(coord, player):
  '''checks if square of 4 adjacent pieces, returns true if square made'''
  try:
      if board[coord[0]-1][coord[1]] == player and board[coord[0]-1][coord[1]+1] == player and board[coord[0]][coord[1]+1] == player:
          return True
  except:
      pass
  try:
      if board[coord[0]-1][coord[1]] == player and board[coord[0]-1][coord[1]-1] == player and board[coord[0]][coord[1]-1] == player:
          return True
  except:
      pass
  try:
      if board[coord[0]+1][coord[1]] == player and board[coord[0]+1][coord[1]+1] == player and board[coord[0]][coord[1]+1] == player:
          return True
  except:
      pass
  try:
      if board[coord[0]+1][coord[1]] == player and board[coord[0]+1][coord[1]-1] == player and board[coord[0]][coord[1]-1] == player:
          return True
  except:
      pass
  return False

  
def check_for_4(coord, player):
    '''calls other check functions to see if any find 4 in a line/square for the given piece, returns true if at least one is valid, otherwise returns false'''
    has4 = check_sides(coord, player) or check_top_bottom(coord, player) or check_diagonals(coord, player) or check_squares(coord, player)
    return has4

# Display message when a character wins 
def turtle_message(player):
    '''prints a message celebrating winner of the game (black or red)'''
    t.setup(600, 600)
    t.colormode(255)
    t.speed(10)
    t.bgcolor("cyan")
    t.pensize(5)
    t.penup()
    for i in range(100):
        coord1 = r.randint(0,600)-300
        coord2 = r.randint(0,600) - 300
        t.goto(coord1, coord2)
        t.pencolor(r.randint(0,255), r.randint(0,255), r.randint(0,255))
        t.pendown()
        t.right(r.randint(0,180))
        t.forward(5)
        t.penup()

    t.goto(0,-20)
    if player == 'B':
        t.pencolor(0,0,0)
        t.write("Black\nwins!", align = "center", font=("Verdana", 100, "bold"))
    else:
        t.pencolor(250,0,0)
        t.write("Red\nwins!", align = "center", font=("Verdana", 100, "bold"))
    t.done()



# inital display of instructions and options
display_instructions()
print('\n')
display_options()
print('\n')

#2D array of empty board, filled with '.'
board = read_board_file()

#gets first move for Black
coord = get_move_initial()
num_moves = 0
player = "B"

# while loop for the game, while user does not quit, checks if user wants instrutions
while coord != "q":
    if coord == "r":
        display_instructions()
    elif coord == "o":
        display_options()
    elif coord == "d":
        display_board()
    else:
        #assigns player to space, counts moves
        board[coord[0]][coord[1]] = player
        num_moves+=1
        #once all pieces for a player are placed, starts checking for line/square
        if num_moves>=7:
            isOver = check_for_4(coord, player)
            if isOver:
                print(f"{player} won!")
                turtle_message(player)
                break
        #switch players turn
        if player == "B":
            player = "R"
        else:
            player = "B"
    #different move conditions if all players are placed, checks which is case and calls proper function
    if num_moves>=8:
        coord = get_moves(board, player)
    else:
        coord = get_move_initial()

else:
    print("You have quit the game!")




#Good job, players! <333
