#!/usr/bin/env python
# coding: utf-8

# ### Tic Tac Toe
# For your milestone project you will create a Tic Tac Toe game for 2 human players
# 
# 2 players should be able to play the game(both sitting at the same computer)
# 
# The board should be printed out everytime a player makes a move
# 
# you should be able to accept input of player position and then place a symbol on the board

# Step 1: Write a function that can print out a board. set up your board asa list, here each index 1-9 corresponds with a number on a number pad, so you get 3 by 3 board representation

# ##### Tic Tac Toe Project Helpful Hints
# 
# In this text lecture we will just have a useful guide for helping you complete the project! Sometimes this project can feel overwhelming, like being thrown into the deep end of the pool and told "Now learn to swim!". So to help out with this, here's a guide to help you begin in the right direction! (Note, there's lots of ways to accomplish this task, so your code may look completely different than the given solution). If the hints below still aren't enough, check out the "Walkthrough Workbook" notebook for even more help!
# 
# First off, make sure you understand the project scope. What needs to happen?
# 
# 
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.
# Ok so we got a general idea of what we need to do. Let's break it down by steps. If you're having trouble with the project, come and check this lecture if you ever get stuck.
# 
# ##### PROJECT HINTS:
# 
# 
# Start by deciding how you will store the player's marker positions (Xs and Os). Let's choose a list, where each index corresponds with a number on a keypad, which in turn corresponds with a position on the 3 by 3 board.
# Create a list called board which will keep track of the player markers.
# The list should already be the same length as your intended board.
# Create a function that will print a board. Not just the list, but an actual representation of a board! This can be done with multiple print statements within the function. Think about how you would take elements from the list and print them out into the board. (You can also clear output in jupyter notebook with clear_output() . You need to import this, so at the top of a cell copy and paste: from IPython.display import clear_output
# Write a function which takes an input marker string 'X' or "O' and a given number and stores it to a list at that appendix.
# You might have to look up how to take input in python! input()
# Play around with input() to make sure you understand it
# Write a function that takes in the board and a player marker and checks it theres a win or a tie.
# The checking for a win should be a series of a bunch checks, for example: (board[7] == board[8] == board[9] == marker)would check the first top row if they all match a player's marker.
# Check for a tie (this means nobody won and the board list is full!)
# Now begin writing functions that begin game play.
# You'll need to write a function which starts combining and calling the different functions you've made within it.
# For example, a function which asks for a player's move, then updates the board,then checks for a win, then prints out the board.
# How can you keep the game continually going?
# Maybe try using a while loop.
# Something like, while the board isn't full and nobody's won...
# You might want to think about how to use boolean objects as markers of the game's status.
# Alright you should have enough now to begin piecing things together!
# If you're still stuck, try googling around for "Python Tic Tac Toe" for ideas of how to put all your pieces and functions together!
# Great job and remember, this is a milestone project, so its meant to be challenging!
# 
# 
# 
# Other things that you may want to implement:
# 
# 1. Taking in a player's input:
# 
# If you're confused on how to take in a players input, you have to use input() for Python 3, or raw_input() for Python 2.. You can use it in the following manner:
# 
# board_position = input("Please enter a number for the board position choice: ")
# 
# Then you would see a pop-up occur with a text box asking you for your input. Type in the number and press enter, now the variable board_position is an integer you can use for your code. For more on the differences between raw_input() and input(), check out this answer.
# 
# 2. Checking an input and asking again:
# 
# In my solution I take into account if a player possibly puts in an incorrect input (like passing a string 'hello' when asked for their board position choice). You can take care of this by using a while loop!

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|' +board[8]+'|'+board[9])
    print ("-|-|-")
    print(board[4]+'|' +board[5]+'|'+board[6])
    print ("-|-|-")
    print(board[1]+'|' +board[2]+'|'+board[3])


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# Test Step 1: run your function on a test version of the board list, and make adjustments as necessary

# In[3]:


test_board = [" "]*10
display_board(test_board)


# Step 2: write a function that can take in a player input and assign their markers as "X" or 'O'. Think about using while loops to continually ask untill you get a correct answer

# In[ ]:


def player_input():
    '''
    OUTPUT = (player 1 marker, player 2 marker)
    '''
    marker = ''
    # keep Asking Player1 to choose X or O
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('player 1, choose X or O: ').upper()
        
    if marker == 'X':
        return ('X', 'O')
   
    else:
        return ('O','X')
        
   


# Test Step 2 : run the function to make sure it returns the desired output

# In[11]:


player1_marker, player2_marker = player_input()


# In[12]:


# you can use tuple unpacking the following way


# In[13]:


player2_marker


# #

# #### Step 3 
# - write a function that takes in the board list object, a marker('X' or 'O') , and a desired positon (number 1-9) and assign it to the board

# In[15]:


def place_marker(board, marker, position):
    
    board[position] = marker


# #### Test Step 3:
# - Run the place marker function using test patameters and display the modified board

# In[16]:


place_marker(test_board, '$',8)
display_board(test_board)


# #### Step 4: is to write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

# In[17]:


def win_check(board, mark):
    # we have to ask what is is it to win tic tac toe?
    
    # All Rows , and check to see if they all share the same marker? 
    return((board[1] ==mark and board[2] ==mark and board[3] ==mark) or
    (board[4] ==mark and board[5] ==mark and board[6] ==mark) or
    (board[7] ==mark and board[8] ==mark and board[9] ==mark) or
    (board[1] ==mark and board[4] ==mark and board[7] ==mark) or
    (board[2] ==mark and board[5] ==mark and board[8] ==mark) or
    (board[3] ==mark and board[6] ==mark and board[9] ==mark) or
    (board[1] ==mark and board[5] ==mark and board[9] ==mark) or
    (board[3] ==mark and board[5] ==mark and board[7] ==mark))
    
    #All columns , and check to see if they all share the same marker? 
    
    # finally, we have 2 diagonals to check matching


# In[19]:


display_board(test_board)
win_check(test_board, 'X')


# #### Step5: 
# - write a function that uses the random module to randomly decide whic player goes first. You may want to lookup random.randint() return a string of which player went first.

# In[20]:


# we can use random.randint() just pass 0 or 1 and we can just use it as coin flip
import random 
def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# ##### Step 6: 
# - Write a function that returns a boolean indicating whether a space on the board is freely available - for our case it means an empty string

# In[21]:


def space_check(board, position):
    
    return board[position]== ' '


# ##### Step 7: 
# - Write a function that checks if the board is full and return a bookean value. True if full, False otherwise

# In[22]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    # Board is full if we return True
    return True


# ##### Step 8: Write a function that asks for a players next position( as a number 1-9) and then use the function form step 6 to check if its a free position. if it is, then return the position for later use

# In[23]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('choose a position:(1-9)'))
        
    return position


# #### Step:9
# - write a function that asks the player if they want to play again and returns a boolean True if they do want to play again

# In[24]:


def replay():
    
    choice = input('play again? Enter Yes or No')
    
    return choice == 'Yes'


# ### Step 10:  hardest part we have to code out all the LOGIC! 
# #####   - Use While Loops and the Functions you've made to run the game!

# In[31]:


# While loop to keep Running The Game!
print('Welcome to Tic Tac Toe! ')

while True:
    
    # Play the game here
    
    ## Set everything up like board, who's First, choose markers etc
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Ready to play- y or n? ')
    
    if play_game == 'y':
        game_on = True
        
    else:
        game_on = False
    ## game play
    
    while game_on:
        
        if turn == 'player 1':
            
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Has Won! ! ')
                
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'
                    
            
    
        else:
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 Has Won! ! ')
                
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'
    
        ### player Two Turn
    
    if not replay():
        break
    


# In[32]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




